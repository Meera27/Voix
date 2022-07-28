const express = require("express");
const homeRouter = express.Router();

function router() {
    homeRouter.get("/test", function (req, res) {
      res.render("home", {
      });
      
    });
    return homeRouter;
}

module.exports = router;