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

const put_nn_predicted_online_data = {
  name: 'put_nn_predicted_online_data',
  text: 'INSERT INTO nn_predicted_online_data (mtime, p_x_1, p_y_1, p_x_2, p_y_2, device_id, beacons_mac, rssi) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)'
}

const put_smartphone_data_all = {
  name: 'put_smartphone_data_all',
  text: 'INSERT INTO smartphone_data_all (time, x, y, dev_id, addresses, rssi_avg) VALUES ($1, $2, $3, $4, $5, $6)'
}

const client = new Client({
  user: 'db)user',
  host: '11.11.11.11',
  database: 'db_name',
  password: 'db_pass',  
  port: 5432,
})
client.connect();

var putData2DB_proto = grpc.loadPackageDefinition(packageDefinition).ips_data_exchange;

function putData2DB(call, callback) {

  let date = new Date();
  let y = date.getFullYear();
  let m = date.getMonth()+1;
  let d = date.getDate();
  let h = date.getHours();
  let min = date.getMinutes();
  let s = date.getSeconds();
  let sdate = "" + y + "-" + m + "-" + d + " " + h + ":" + min + ":" + s;

  console.log("putData2DB p_frst_x: " + call.request.p_frst_x)
  console.log("putData2DB p_frst_y: " + call.request.p_frst_y)
  console.log("request.dev: " + call.request.devserial)
  
  client.query(put_nn_predicted_online_data, [sdate, call.request.p_frst_x, call.request.p_frst_y, call.request.p_scnd_x, call.request.p_scnd_y, call.request.devserial, call.request.addr, call.request.rssi], (err, res) => {
      if (err) {
        console.log(err.stack)
      } else {
        //console.log("data was added to DB with data id: " + data_id)
      }
  })
  callback(null, {message: 'callback from node server '});
  
}

function main() {
  var server = new grpc.Server();
  server.addService(putData2DB_proto.Putter.service, {putData2DB: putData2DB});
  server.bind('0.0.0.0:50052', grpc.ServerCredentials.createInsecure());
  server.start();
}
main();
