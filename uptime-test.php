<?php




$api_key_demo = "m776861145-d60d8f272b3b299802ea4af8"; 
$api_key_www = "m776861146-97cc8bd376321f69e6286cfc";

function getMonitor($api_key){

  $server = "https://api.uptimerobot.com/getMonitors?apiKey=" . $api_key . "&format=json"; 
  $server2 = file_get_contents($server); 
  if(substr($server2, 0, 19) == 'jsonUptimeRobotApi(' && substr($server2, -1, 1) == ')'){
	$json = substr($server2, 19, strlen($server2) - 20);
	if(!is_null($json)) {
	    $obj = json_decode($json);
	    $nameMon =  $obj->monitors->monitor[0]->friendlyname;
	    $uptimePerc = $obj->monitors->monitor[0]->alltimeuptimeratio;
            $statusMon =  $obj->monitors->monitor[0]->status;

	    print "<!-- Disabled for now \r\n";
	    print "Monitor Name: <b>".$nameMon."</b><br>\r\n";
	    print "";
            if($statusMon == '2'){
	        print "Monitor Status : Server is <b>up</b><br>\r\n";
	    }else{
		print "Monitor Status: Server is <b>down</b><br>\r\n";
            }
	    print "Server Uptime %: <b>".$uptimePerc."</b><br>\r\n";
	    print " -->";
	}
  }

}

$mon1 = getMonitor($api_key_demo);
$mon2 = getMonitor($api_key_www);

print $mon1;
print $mon2;

?>
