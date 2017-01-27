var express = require('express');
var fs = require('fs');
var path = require('path');

var server = express();

server.get('/', function(req, res) {
    var db = fs.readFileSync(path.join(__dirname, 'db', 'db.js'));
    db = JSON.parse(db);

    if (!db.count) {
        db.count = 1;
    }
    
    db.count++;

    fs.writeFileSync(path.join(__dirname, 'db', 'db.js'), JSON.stringify(db));

    res.send(db.count.toString());
});

server.get("/hanzohap", function(req, res) {
    res.readFile('HZHwebsite.png');
    res.send("HZHwebsite.png");
});

server.listen(8080);