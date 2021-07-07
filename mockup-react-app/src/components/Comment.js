import React from "react";
import { useState } from "react";
import { Divider, Avatar, Grid, Button, Paper } from "@material-ui/core";
import TranslateIcon from "@material-ui/icons/Translate";
import * as axios from "axios";

const imgLink =
  "http://www.gravatar.com/avatar/3b3be63a4c2a439b013787725dfce802?d=identicon";

function Comment({ comment }) {
  const [message, setMessage] = useState(comment.msg);

  const translate = async () => {
    await axios
      .post(
        "https://qxjfzvn520.execute-api.eu-central-1.amazonaws.com/translate",
        { message: comment.msg, target_language: "ru" }
      )
      .then(function (res) {
        console.log(res);
        setMessage(res.data.translated_message);
      });
  };

  return (
    <Paper style={{ padding: "40px 20px" }}>
      <Grid container wrap="nowrap" spacing={2}>
        <Grid item>
          <Avatar alt="Remy Sharp" src={imgLink} />
        </Grid>
        <Grid justifyContent="left" item xs zeroMinWidth>
          <h4 style={{ margin: 0, textAlign: "left" }}>{comment.name}</h4>
          <p style={{ textAlign: "left" }}>{message}</p>
          <p style={{ textAlign: "left", color: "gray" }}>
            posted {comment.ago} minutes ago
          </p>
        </Grid>
        <Grid item>
          <Button variant="outlined" color="default" onClick={translate}>
            <TranslateIcon />
          </Button>
        </Grid>
      </Grid>
      <Divider variant="fullWidth" style={{ margin: "30px 0" }} />
    </Paper>
  );
}

export default Comment;
