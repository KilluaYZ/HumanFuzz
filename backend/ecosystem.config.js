module.exports = {
  apps : [{
    name   : "Readio-Server",
    script : "cd /home/killuayz/codecheck-2nd-genration-server && flask --app codecheck run -h \"::\" -p 5000 ",
    error_file: "/home/killuayz/codecheck-2nd-genration-server/error.log",
    out_file: "/home/killuayz/codecheck-2nd-genration-server/out.log"
  }]
}
