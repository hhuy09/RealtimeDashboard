var port = 8080;
 
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
 
var kafka = require('kafka-node');
var topic = 'Second_Topic';
var client = new kafka.KafkaClient('localhost:2181', "consumer-" + Math.floor(Math.random() * 10000));
var topicSet = [{ topic: topic }];
var consumer = new kafka.Consumer(client, topicSet);
 
 
app.get('/', function(req, res){
    //res.sendFile(path.join(__dirname, 'web', 'index.html'));
    //res.sendFile('index.html', { root: path.join(__dirname, 'web') });
    res.sendFile('web/index.html', {root: __dirname});
});
 
io = io.on('connection', function(socket){
    console.log('a user connected');
    socket.on('disconnect', function(){
        console.log('a user disconnected');
    });
});
 
//collect data from Kafka via Second_Topic and emit them to clients
consumer = consumer.on('message', function(data){
    value = JSON.parse(data.value);
    console.log(value);

    io.emit("aggregator-message", value);
});
 
 
http.listen(port, function(){
    console.log("Running on port http://localhost:" + port)
});