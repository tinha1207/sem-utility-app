import { Typography, Grid, Button, TextField, Input } from "@material-ui/core";
import React from "react";
import Layout from "../../components/Layout";
import Head from "next/head";
import { useState } from "react";
import useStyles from "../../utils/styles";
import AccountUploadForm from "../../components/AccountUploadForm";
import TemplateButton from "../../components/TemplateButton";

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
          <Grid container className={classes.main}>
            <Grid item>
              <AccountUploadForm />
            </Grid>
          </Grid>
          <Grid item>
            <TemplateButton />
          </Grid>
        </Grid>
      </Layout>
    </>
  );
};

export default Keyword;
