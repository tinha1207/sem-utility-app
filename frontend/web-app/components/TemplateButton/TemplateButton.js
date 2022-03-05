import { Button } from "@material-ui/core";
import React from "react";
import useStyles from "../../utils/styles";
import axios from "axios";

const TemplateButton = () => {
  const classes = useStyles();
  const url = "http://localhost:8000/utility/iso_keyword/template";

  const onDownload = () => {
    axios
      .get(url, {
        responseType: "arraybuffer",
      })
      .then((response) => {
        const tempUrl = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = tempUrl;
        link.setAttribute("Download", "template.xlsx");
        document.body.appendChild(link);
        link.click();
      });
  };

  return (
    <Button
      className={classes.button}
      variant="contained"
      size="small"
      color="secondary"
      onClick={onDownload}
    >
      Download Template
    </Button>
  );
};

export default TemplateButton;
