const express = require("express");
const UserData = require("../model/userdata");
const loginRouter = express.Router();
const {spawn} = require('child_process');
let p = require('python-shell');
const bcrypt = require('bcrypt')

let newpass= "alberteinstein"
function router() {
  loginRouter.get("/", function (req, res) {
    res.render("login", {
      error: "",
      title: "Login",
    });
  });
  // loginRouter.post("/valid", async(req, res) => {


    loginRouter.post("/valid", function(req, res){
      var email = req.body.email;
      var password = req.body.password;

      UserData.findOne({email:email})
      .then(function(user){
        bcrypt.compare(password,user.password,function(err,result){
          if(result){
            res.redirect("/home");
              var dataToSend;
              const python = spawn('python', ['app.py',email,password]);
              python.stdout.on('data', function (data) {
              console.log('Pipe data from python script ...');
              dataToSend = data.toString();
            });
              python.on('close', (code) => {
              console.log(`child process close all stdio with code ${code}`);
              res.send(dataToSend)
            });
          }
          else {
            if (!result) {
              var dataToSend;
              const python = spawn('python', ['login.py']);
              python.stdout.on('data', function (data) {
              console.log('Pipe data from python script ...');
              dataToSend = data.toString();
            });
              console.log(password)
              res.render("login", {
                error: "Invalid Login!!!",
                title: "Login",
              });
            } else {
              console.log(err);
            }
          }
        })
      })

    // var email = req.body.email;
    // var password = req.body.password;  
    // var pa = bcrypt.hash(req.body.password,10)
    // let isEqual = await bcrypt.compare(req.body.password,newpass)
    // console.log(pa)
    // UserData.findOne(
    //   { email: email, 
    //     password: password},
    //   function (err, user) {
    //     if(user) {
    //       console.log("From db "+user.fname)
    //       res.redirect("/home");
    //           var dataToSend;
    //           const python = spawn('python', ['app.py',email,password]);
    //           python.stdout.on('data', function (data) {
    //           console.log('Pipe data from python script ...');
    //           dataToSend = data.toString();
    //         });
    //           python.on('close', (code) => {
    //           console.log(`child process close all stdio with code ${code}`);
    //           res.send(dataToSend)
    //         });
    //     } else {
    //       if (!user) {
    //         console.log(password)
    //         res.render("login", {
    //           error: "Invalid Login!!!",
    //           title: "Login",
    //         });
    //       } else {
    //         console.log(err);
    //       }
    //     }
    //   }
    // );
  });




  return loginRouter;
}
module.exports = router;