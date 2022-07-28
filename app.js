const express = require("express");
const app = new express();
const port = process.env.PORT || 3000;
const signupRouter = require("./src/routes/signuproutes")();
const loginRouter = require("./src/routes/loginroutes")();
const homeRouter = require("./src/routes/homeroutes")();

const {spawn} = require('child_process');
app.use(express.urlencoded({ extended: false }));
app.use(express.static("./public"));
app.set("view engine", "ejs");
app.set("views", __dirname + "/src/views");
app.use("/signup", signupRouter);
app.use("/login", loginRouter);
app.use("/home", homeRouter);


app.get('/',function(req,res){
  res.render("signup");
})
app.get('/home', (req, res) =>{
  res.render("home");
  var dataToSend;
  const python = spawn('python', ['app.py']);
  python.stdout.on('data', function (data) {
  console.log('Pipe data from python script...');
  dataToSend = data.toString();
  }); 
})

app.get('/signup',function(req,res){
  res.render("signup");
})

app.get('/login',function(req,res){
  res.render("login");
})
app.listen(port, function () {
    console.log("Ready at " + port);
  });

