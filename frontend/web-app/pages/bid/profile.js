import React, { useEffect, useState } from "react";
import useStyles from "../../utils/styles";
import Layout from "../../components/Layout";
import { Grid, Typography } from "@material-ui/core";
import GetBidProfiles from "../../services/GetBidProfiles";

const Profile = () => {
  const classes = useStyles();
  const [bidProfiles, setBidProfiles] = useState([]);
  useEffect(() => {
    let data = GetBidProfiles();
    console.log(data);
  }, []);
  return (
    <>
      <Layout title="Bid Profile" />
      <Grid container className={classes.main}>
        <Typography variant="h2">Bid Profile</Typography>
      </Grid>
    </>
  );
};

export default Profile;
