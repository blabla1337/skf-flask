# RFD and file download injections
-------

## Example:


    /*
    the following code snippet represents the jsf page used to download a file 

    <html xmlns="http://www.w3.org/1999/xhtml"
        xmlns:h="http://java.sun.com/jsf/html"
        xmlns:f="http://java.sun.com/jsf/core"
        xmlns:p="http://primefaces.org/ui"
        xmlns:cu="http://localhost:8080/custom"
        xmlns:ui="http://java.sun.com/jsf/facelets">

    <f:view contentType="text/html">
    <h:head>
        <h:outputStylesheet name="common-style.css" library="css" />
    </h:head>   
    <h:body>
        <div id="page">    
                <div id="header">
                <ui:insert name="header" >
                    <ui:include src="commonHeader.xhtml" />
                </ui:insert>
                    <img src="resources/images/skf.png"></img>
                </div>
                <p:separator style="border: 0px;"></p:separator>
        </div>
        
        <div id="content">      
            <ui:insert name="content" >
            <ui:include src="commonDownloadRFD.xhtml" />
            </ui:insert>      
            <p:dialog modal="true" widgetVar="statusDialog" header="Status" draggable="false" closable="false" resizable="false">
                <p:graphicImage name="/images/ajaxloadingbar.gif" />
            </p:dialog>
            
            <h:form>
                <p:commandButton value="Download" ajax="false" actionListener="#{fileDownloadController.filedownload}" onclick="PrimeFaces.monitorDownload(start, stop);" icon="ui-icon-arrowthick-1-s">
                </p:commandButton>
                <p:spacer width="20" height="40" />
                <p:commandButton action="#{navigationController.moveToMainMenu}" ajax="false" value="Main Menu" />    
            </h:form>
            
            <script type="text/javascript">
                    function start() {
                        PF('statusDialog').show();
                    }
                    
                    function stop() {
                        PF('statusDialog').hide();
                    }
            </script>
        </div>
    </h:body>
    </f:view>
    </html>

    */


    // The following bean represents the managed bean to perform the file download action   

    package prime.com.beans;

    import java.io.File;
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.io.OutputStream;
    import java.sql.Connection;
    import java.sql.PreparedStatement;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.time.LocalDateTime;
    import org.apache.log4j.Logger;
    import java.util.regex.Pattern;

    import javax.faces.application.FacesMessage;
    import javax.faces.bean.ManagedBean;
    import javax.faces.component.UIComponent;
    import javax.faces.context.ExternalContext;
    import javax.faces.context.FacesContext;
    import javax.naming.Context;
    import javax.naming.InitialContext;
    import javax.naming.NamingException;
    import javax.servlet.annotation.MultipartConfig;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    import javax.sql.DataSource;

    import com.Lib.AuditLog;
    import com.Lib.InputValidation;
    import com.Lib.WhiteList;
    

    @ManagedBean(name="fileDownloadController")
    @MultipartConfig
    public final class FileDownloader {
        
        // Applications are rarely tested for Unicode exploits, and yet many are vulnerable due to the same sort of issues which allows HTTP Request Smuggling to work – every browser, 
        // web server, web application firewall or HTTP inspection agent, and other device treats user locale handling in different (and usually confusing) manner.
        // Canonicalization deals with the way in which systems convert data from one form to another. 
        // Canonical means the simplest or most standard form of something. Canonicalization is the process of converting something from one representation to the simplest form.
        // Web applications have to deal with lots of canonicalization issues from URL encoding to IP address translation. 
        // When security decisions are made based on less than perfectly canonicalized data, the application itself must be able to deal with unexpected input safely. 
        
        final static Logger logger = Logger.getLogger(FileUploader.class);
        private AuditLog Log = new AuditLog(); 
        private WhiteList wl = new WhiteList();
        InputValidation validate = new InputValidation();
        private UIComponent component;
        private String file;
        private File fileplace;
        
        public FileDownloader() {        
            
            FacesContext context = FacesContext.getCurrentInstance();
            HttpServletRequest request = (HttpServletRequest)FacesContext.getCurrentInstance().getExternalContext().getRequest();
            HttpServletResponse response = (HttpServletResponse) FacesContext.getCurrentInstance().getExternalContext().getResponse();  
            
            // Unicode Encoding is a method for storing characters with multiple bytes. Wherever input data is allowed, 
            // data can be entered using Unicode to disguise malicious code and permit a variety of attacks. RFC 2279 references many ways that text can be encoded. 
            
            FacesContext.getCurrentInstance().getExternalContext().setResponseContentType("text/html;charset=UTF-8");
            
            String action = ""; 
            boolean proceed = false ;
            String mimetype = "";
            
            // Create path components to save the file
            // The location of stored files should always be outside of your root
            file = "C:\\tsec.jpg";
            fileplace = new File(file); 
            
            String fileNameformat = fileplace.getName();
            
            String filenameparts[] = fileNameformat.split(Pattern.quote("."));
            String fileName = filenameparts[0];
            String afterdot = filenameparts[1];
            
            /*
            First we check if the value is alphanumeric only to prevent uploading out of intended directory, 
            as well as other injections
            */
            
            /* in normal situations the userID should be retrieved from session or from the web page made the request. 
            * For demonstration purposes we assume that the usedID is always 2, which indicated the Administration ID number. 
            */
            
            if (validate.validateInput("2", fileName, "alphanummeric", "validation failed",request.getRemoteAddr(),"HIGH") == "validation failed")
            {
            proceed = false;
            action = "validation failed";
            }
            
            else if (validate.validateInput("2", fileName, "alphanummeric", "Session Termination",request.getRemoteAddr(),"HIGH") == "terminate")
            {
                proceed = false;
                action = "terminate";
            }   
            
            else if (validate.validateInput("2", fileName, "alphanummeric", "Block access",request.getRemoteAddr(),"HIGH") == "block")
            {
                proceed = false;
                action = "block";
            }else{
                Log.SetLog("2", "Validated Successfully" , "SUCCESS", LocalDateTime.now(),request.getRemoteAddr(),  "");
                action = "Validated Successfully";
                proceed = true;
            }
            
            if (proceed == true)
            {
                //Here we connect to the database by means of a connection string as configured in the web.xml and /META-INF/context.xml 
                Connection conn = null;
                try {
                            
                    Context initContext = new InitialContext();
                    Context webContext  = (Context)initContext.lookup("java:/comp/env");
                    DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
                    conn = ds.getConnection();  

                    //Here we select the number of counts from aggregate column in order to verify the number of connections:
                    String query = "SELECT * FROM privileges WHERE privilegeID=?";
                
                    PreparedStatement st = conn.prepareStatement(query);
                    
                    /* in normal situations the privilegeID should be retrieved from database based on UserID retrieved from the active session 
                    * or from the web page made the request. 
                    * For demonstration purposes we assume that the privilegeID is always 1, which indicated the Administration privilege ID number. 
                    */
                    st.setString(1, "1");

                    // execute the query, and get a java result set
                    //We bind the parameter in order to prevent SQL injections
                    ResultSet rs = st.executeQuery();
                    
                    while (rs.next())
                    {
                        mimetype   = rs.getString("mimeType");
                    }
                    st.close();
                    conn.close();
                } catch (SQLException | NamingException e) {
                    logger.error("cannot read from database. check query :" e.toString());
                }     

                /*
                We also define the mime-type per download file.
                This is because whenever a user can only download images it is not necessary to set
                an uncommon content-type header for it.
                NOTE: These mime-types should not be stored based upon the mime-type which was send 
                the response header when the user uploaded the file. This value can be easily 
                manipulated with an intercepting PROXY. You should get the mime-type from the file
                itself after it was stored on the server.
                */
                response.reset();
                response.setContentType(mimetype);
                response.addHeader("Cache-Control", "no-cache");
                response.addHeader("Content-Disposition", "attachment; filename=" + fileName + "." + afterdot + ";");
                
                OutputStream out;
                try {
                    out = response.getOutputStream();
                    
                    FileInputStream in = new FileInputStream(fileplace);
                    byte[] buffer = new byte[4096];
                    int length;
                    while ((length = in.read(buffer)) > 0){
                        out.write(buffer, 0, length);
                    }
                    in.close();
                    out.flush();   
                } catch (IOException e) {
                    logger.error("Cannot download file - " e.toString());
                }
            }
            else if (file == null)
            {
                action = "empty";
            }
            
            if (action.equals("terminate"))
            {
                request.getSession().invalidate();
                request.setAttribute("msg","Session terminated! file has not been downloaded");             
                ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
                try {
                    ec.redirect(ec.getRequestContextPath() + "/Menu.xhtml");
                } catch (IOException e) {
                    logger.error("Cannot redirect - " e.toString());
                }
            }
            if (action.equals("validation failed"))
            {
                request.getSession().invalidate();
                context.addMessage(component.getClientId(), new FacesMessage(FacesMessage.SEVERITY_ERROR, "FAIL!", "Session terminated! file has not been downloaded"));
            }
            if (action.equals("block"))
            { 
                request.getSession().invalidate();          
                context.addMessage(component.getClientId(), new FacesMessage(FacesMessage.SEVERITY_ERROR, "FAIL!", "Session terminated with Blocked Access! file has not been downloaded"));
            }
            if (action.equals("Validated Successfully"))
            {
                context.addMessage(component.getClientId(), new FacesMessage(FacesMessage.SEVERITY_ERROR, "SUCCESS!", "file downloaded"));   
            }
        }
        
        public String getFile() {
            return file;
        }

        public void setFile(String file) {
            this.file = file;
        }

        public void fixedDownloads(String file, String download, HttpServletResponse response)
        {
            /*
            The second example is for whenever you are providing users with fixed downloads
            such as manuals etc. We do not only check if the file just exists, because that would
            allow an attacker to also download important other files from your server, so instead
            we white-list them.
            */
            if (wl.WhiteListing(file, download) != false)
            {
                response.reset();
                response.setContentType("text/plain");
                response.addHeader("Cache-Control", "no-cache");
                response.addHeader("Content-Disposition", "attachment; filename=" + file + ";");
                
                OutputStream out;
                try {          
                    out = response.getOutputStream();
                    FileInputStream in = new FileInputStream(file);
                    byte[] buffer = new byte[4096];
                    int length;
                    while ((length = in.read(buffer)) > 0){
                        out.write(buffer, 0, length);
                    }
                    in.close();
                    out.flush();
                } catch (IOException e) {
                    logger.error("Cannot download file - " e.toString());
                }   
            }   
        }
    }

