import { Typography, Grid, Button, TextField, Input } from "@material-ui/core";
import React from "react";
import Layout from "../../components/Layout";
import Head from "next/head";
import { useState } from "react";
import useStyles from "../../utils/styles";
import AccountUploadForm from "../../components/AccountUploadForm";

const Keyword = () => {
  const classes = useStyles();

  // let bodyFormData = new FormData();

  const onDownload = () => {
    const link = document.createElement("a");
    link.download = "../../public/static/templates/iso_template.xlsx";
    link.href = "../../public/static/templates/iso_template.xlsx";
    link.click();
  };
  return (
    <>
      <Layout title="Keyword Iso Tool">
        <Grid container className={classes.main}>
          <Typography variant="h2">Keyword Isolation Tool</Typography>
          <Grid container>
            <Grid item>
              <AccountUploadForm />
            </Grid>
          </Grid>
          <Grid item>
            <Button
              className={classes.button}
              variant="contained"
              size="small"
              color="secondary"
              onClick={onDownload}
            >
              Download Template
            </Button>
          </Grid>
        </Grid>
      </Layout>
    </>
  );
};

export default Keyword;
