const mongoose = require("mongoose");
const bcrypt = require("bcryptjs")
mongoose.connect('mongodb://localhost:27017/Voice');

const Schema = mongoose.Schema;

const UserSchema = new Schema({
  fname: String,
  lname: String,
  phone: Number,
  email:
  {type: String,
  required:true,
  unique:true},

  emailToken:{
    type:String,
  },
  isVerified:{
    type:Boolean,
  },
  password: String,
});

var UserData = mongoose.model("userdata", UserSchema);

module.exports = UserData;