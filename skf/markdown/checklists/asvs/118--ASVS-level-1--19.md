9.4 Verify that the application sets appropriate anti-caching headers as per the risk of the application, such as the following:
    Expires: Tue, 03 Jul 2001 06:00:00 GMT 
    Last-Modified: {now} GMT
    Cache-Control: no-store, no-cache, must-revalidate, max-age=0 Cache-Control: post-check=0, pre-check=0
    Pragma: no-cache