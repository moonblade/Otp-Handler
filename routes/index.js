var express = require('express');
var router = express.Router();

/* GET home page. */
let data = {}
router.get('/', function(req, res, next) {
  const { mobile } = req.query;
  if (!data[mobile]) { data[mobile] = {}}
  res.send(data[mobile]);
});

router.post("/", (req, res, next) => {
  if (!req.body.otp || !req.body.mobile)
    return res.status(400).end()
  otp = req.body.otp;
  mobile = req.body.mobile;
  lastTime = Date.now()
  data[mobile] = { otp, lastTime }
  res.status(200).end()
})

module.exports = router;
