const express = require('express');
const signupRouter = express.Router();
const UserData = require('../model/userdata');
const bcrypt=require('bcrypt')
var crypto =require('crypto');
const jwt = require('jsonwebtoken')
const nodemailer = require('nodemailer');
const {spawn} = require('child_process');

hashedPass = ''
function router(){
    signupRouter.get('/',function(req,res){
        res.render('signup',{
            email:"",
            error:"",
        })
    });
    signupRouter.post('/auth',async (req,res)=>{
         var password = req.body.password
         var email =  req.body.email,
         fname =req.body.fname
         var dataToSend;
        const python = spawn('python', ['script.py',email,password,fname]);
        python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
        // await res.redirect("/signup")
            });
         var messg = "";
         bcrypt.hash(password,12, function(err,hash){
            var email = req.body.email;
            UserData.findOne({"email":email})
            .then(function(users){
                if(users){
                    var dataToSend;
                    const python = spawn('python', ['exist.py']);
                    python.stdout.on('data', function (data) {
                    console.log('Pipe data from python script...');
                    dataToSend = data.toString();
  }); 
                    res.render('signup',{
                        
                                email:email,
                                error:"is already associated with another account.",
                            }
                            )
                }
                else if(user == null && users == null){
                    console.log("Success");
                    var user = {
                        fname : req.body.fname,
                        lname : req.body.lname,
                        phone : req.body.phon,
                        email : req.body.email,
                        password : hash
                    }
                    var user = new UserData(user);
                    user.save()  
                    messg = "Success";
                    return res.status(200).redirect('/login')
                } 
            }) // findone.then
        })
       
        });
    return signupRouter;
}
module.exports = router;

 // var password = await bcrypt.hash(req.body.password,10);
        //  UserData.findOne({email:email},async(err,user)=>{
        //     try{
        //      if(user){
        //         res.render('signup',{
        //             email:email,
        //             error:"is already associated with another account.",
        //         })
        //         console.log("Invalid!!")
        //      }
        //      else if(err){
        //          console.log(err);
        //      }
        //      else if(!user){
        //         const newuser = {fname,lname,phone,email,password,
        //     };
        //         console.log(newuser);
        //         UserData.create(newuser);
        //         return res.status(200).redirect('/login')}
        //      }
        //      catch(er){
        //         console.log(err);
        //      }
        //  })