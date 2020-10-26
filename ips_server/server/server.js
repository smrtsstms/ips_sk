var PROTO_PATH = __dirname + '/putData2DB.proto';
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
const {Client} = require('pg');

var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

const put_data_xy_other = {
  name: 'put_data_xy_other',
  text: 'INSERT INTO raw_data_xy_other (mtime, coord_x, coord_y, device_id, beacons_mac, rssi) VALUES ($1, $2, $3, $4, $5, $6)'
}

const put_smartphone_data_all = {
  name: 'put_smartphone_data_all',
  text: 'INSERT INTO raw_data_xy (mtime, coord_x, coord_y, device_id, beacons_mac, rssi, altitude, gyroscope, magnitude) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)'
}

const client = new Client({

  user: 'db_user',
  host: '11.11.11.11',
  database: 'db_name',
  password: 'db_pass',  
  port: 5432,
})
client.connect();

var putData2DB_proto = grpc.loadPackageDefinition(packageDefinition).ips_put_data2db;

function putData2DB(call, callback) {

  let date = new Date();
  let y = date.getFullYear();
  let m = date.getMonth()+1;
  let d = date.getDate();
  let h = date.getHours();
  let min = date.getMinutes();
  let s = date.getSeconds();
  let sdate = "" + y + "-" + m + "-" + d + " " + h + ":" + min + ":" + s;
  let alt = 0.0;
  let gyro = 0.0;
  let mag = 0.0;
  //console.log("putData2DB addr[0]" + call.request.addr)
  console.log("request.dev: " + call.request.dev)

  if(call.request.dev == "OTHER_DEVICE"){

    client.query(put_data_xy_other, [sdate, call.request.x, call.request.y, call.request.devserial, call.request.addr, call.request.rssi], (err, res) => {
        if (err) {
          console.log(err.stack)
        } else {
          //console.log("data was added to DB with data id: " + data_id)
        }
    })
   }
  else if(call.request.dev == "SMARTPHONE"){
    client.query(put_smartphone_data_all, [sdate, call.request.x, call.request.y, call.request.devserial, call.request.addr, call.request.rssi, alt, gyro, mag], (err, res) => {
        if (err) {
          console.log(err.stack)
        } else {
          //console.log("data was added to DB with data id: " + data_id)
        }
    })
  }

  

  
}

function main() {
  var server = new grpc.Server();
  server.addService(putData2DB_proto.Putter.service, {putData2DB: putData2DB});
  server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
  server.start();
}
main();
