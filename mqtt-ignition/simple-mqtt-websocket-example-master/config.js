//host = 'mqtt://q.emqtt.com';	// hostname or IP address
//host = '192.168.1.102';	// hostname or IP address
host = 'localhost';	// hostname or IP address
//port = 1883;
port = 8083;
//port = 15675;
topic = 'Area1/#';		// topic to subscribe to
//topic = 'python/test';		// topic to subscribe to
useTLS = false;
//username = null;
//password = null;
username = "jjolie";
password = "aa";

// path as in "scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]"
//    defaults to "/mqtt"
//    may include query and fragment
//
// path = "/mqtt";
// path = "/data/cloud?device=12345";

cleansession = true;
