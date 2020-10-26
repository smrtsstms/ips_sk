var PROTO_PATH = __dirname + '/putData2DB.proto';
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
var bodyParser = require('body-parser')
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

var putData2DB_proto = grpc.loadPackageDefinition(packageDefinition).ips_data_exchange;
const express = require('express')
const app = express()
const port = //####

var attempts = 0;
var responses = 0;

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

function main() {

 var client = new putData2DB_proto.Exchanger('server_py_client:50051', grpc.credentials.createInsecure());

console.log("express-client started on port: " + port)

  app.post('/appdata', function(req, res, next) {

    let dev = "SMARTPHONE"
    let addr2 = [
          "D1:C5:F3:61:26:1D",
          "D2:E0:A9:D9:04:22",
          "D8:DC:4B:36:5F:EE",
          "CB:57:14:70:4E:18",
          "C2:94:90:41:D2:3D",
          "DF:32:2B:65:93:3E",
          "D7:20:24:DF:82:F0",
          "C7:A5:83:BE:D4:47",
          "EB:FF:39:D3:76:5A"                         
            ];

    let devserial = "";
    let rssi_avg_norm = ["0.9637","0.9637","0.9637","0.9637","0.9637","0.9637","0.9637","0.9637","0.9637"];
    let scAddr;
    let scTime = [];
    let sum = 0;
    let avgRssi = 0;
    let smX = 99;
    let smY = 99;
    
    devserial = req.body.id;
    scDev = req.body.btDevices
    smX = req.body.x;
    smY = req.body.y;
    console.log("Data from device: " + devserial)

    for(var i = 0; i < scDev.length; i++){
      for(var u = 0; u < addr2.length; u++){
        if(scDev[i].address == addr2[u]){
                
          for(var k = 0; k < scDev[i].rssi.length; k++){

            sum = sum + parseFloat(scDev[i].rssi[k]);

            if(k == scDev[i].rssi.length - 1){
              avgRssi = sum/scDev[i].rssi.length/-110;

              rssi_avg_norm[u] = avgRssi;
              sum = 0;
            }
          
          }
        }
      }
    }
    console.log("Data from device: " + devserial)

    client.putData2nn({devserial: devserial, addr: addr2, rssi: rssi_avg_norm}, function(err, response) {
      console.log('Response from python-server:', response);
      //res.send(response.message);
    });    
    
    res.json("OK");
  });

  app.post('/putdata', function (req, res) {
   
    let dev = "OTHER_DEVICE"
    let direction = "";
    let devserial = "";
    let rssi_norm = ["0.9637","0.9637","0.9637","0.9637","0.9637","0.9637","0.9637","0.9637","0.9637"];
    let addr = [
            "d1:c5:f3:61:26:1d",
            "d2:e0:a9:d9:04:22",
            "d8:dc:4b:36:5f:ee",
            "cb:57:14:70:4e:18",
            "c2:94:90:41:d2:3d",
            "df:32:2b:65:93:3e",
            "d7:20:24:df:82:f0",
            "c7:a5:83:be:d4:47",
            "eb:ff:39:d3:76:5a"                     
              ];
    let scannedAddr = [];
    let scannedRssi = [];
 
    x = req.body.x;
    y = req.body.y;
    devserial = req.body.s;
    console.log("Data from device: " + devserial)
    
    scannedAddr[0] = req.body.a1;
    scannedAddr[1] = req.body.a2;
    scannedAddr[2] = req.body.a3;
    scannedAddr[3] = req.body.a4;
    scannedAddr[4] = req.body.a5;
    scannedAddr[5] = req.body.a6;
    scannedAddr[6] = req.body.a7;
    scannedAddr[7] = req.body.a8;
    scannedAddr[8] = req.body.a9;

    scannedRssi[0] = req.body.r1;
    scannedRssi[1] = req.body.r2;
    scannedRssi[2] = req.body.r3;
    scannedRssi[3] = req.body.r4;
    scannedRssi[4] = req.body.r5;
    scannedRssi[5] = req.body.r6;
    scannedRssi[6] = req.body.r7;
    scannedRssi[7] = req.body.r8;
    scannedRssi[8] = req.body.r9;

    for (var i = 0; i < addr.length; i++) {
      //console.log("stage 1")
      for (var j = 0; j < scannedAddr.length; j++) {
        if(scannedAddr[j] == addr[i]){
          rssi_norm[i] =scannedRssi[j]/-110;
        }
      }
    }

    attempts = attempts + 1;
    console.log("attempts: " + attempts)
    client.putData2nn({devserial: devserial, addr: addr, rssi: rssi_norm}, function(err, response) {
      console.log('Response from grpc-server:', response);
      responses = responses + 1;
      console.log("responses: " + responses)      
      //res.send(response.message);
    });

  });

  app.listen(port, () => console.log(`Example app listening on port ${port}!`))

}

main();
