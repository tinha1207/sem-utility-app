import React, { useEffect, useState } from "react";
import useStyles from "../../utils/styles";
import Layout from "../../components/Layout";
import { Grid, Typography } from "@material-ui/core";
import axios from "axios";

const Profile = () => {
  const classes = useStyles();
  const [bidProfiles, setBidProfiles] = useState([]);

  const columns = [
    {
      field: "id",
      headerName: "ID",
      width: 90,
    },
    {
      field: "name",
      headerName: "Name",
      width: 130,
      editable: true,
    },
    {
      field: "note",
      headerName: "Note",
      width: 130,
      editable: true,
    },
    {
      field: "target_acos",
      headerName: "Target Acos",
      width: 90,
      type: "number",
      editable: true,
    },
    {
      field: "min_target_acos_boundary",
      headerName: "Lower Target Acos Boundary",
      width: 130,
      type: "number",
      editable: true,
    },
    {
      field: "max_target_acos_boundary",
      headerName: "Upper Target Acos Boundary",
      width: 130,
      type: "number",
      editable: true,
    },
    {
      field: "max_acos",
      headerName: "Max Acos",
      type: "number",
      width: 130,
      editable: true,
    },
    {
      field: "min_clicks",
      headerName: "Min Clicks",
      type: "number",
      width: 130,
      editable: true,
    },
    {
      field: "min_impressions",
      headerName: "Minimum Impressions",
      type: "number",
      width: 130,
      editable: true,
    },
    {
      field: "floor_bid",
      headerName: "Floor Bid",
      type: "number",
      width: 130,
      editable: true,
    },
    {
      field: "ceiling_bid",
      headerName: "Ceiling Bid",
      type: "number",
      width: 130,
      editable: true,
    },
    {
      field: "increment_up_rate",
      headerName: "Increase Rate",
      type: "number",
      width: 130,
      editable: true,
    },
    {
      field: "increment_down_rate",
      headerName: "Decrease Rate",
      type: "number",
      width: 130,
      editable: true,
    },
    {
      field: "max_increment_up",
      headerName: "Max Increment Up",
      type: "number",
      width: 130,
      editable: true,
    },
    {
      field: "max_increment_down",
      headerName: "Max Increment Down",
      type: "number",
      width: 130,
      editable: true,
    },
  ];

  const rows = bidProfiles.map((row) => ({
    id: row.bid_profile_id,
    name: row.name,
    note: row.note,
    target_acos: row.target_acos,
    min_target_acos_boundary: row.min_target_acos_boundary,
    max_target_acos_boundary: row.max_target_acos_boundary,
    max_acos: row.max_acos,
    min_clicks: row.min_clicks,
    min_impressions: row.min_impressions,
    floor_bid: row.floor_bid,
    ceiling_bid: row.ceiling_bid,
    increment_up_rate: row.increment_up_rate,
    increment_down_rate: row.increment_down_rate,
    max_increment_up: row.max_increment_up,
    max_increment_down: row.max_increment_down,
  }));

  const getBidProfiles = () => {
    const link = "http://localhost:8000/bid/bid_profile";
    axios.get(link).then((response) => {
      const profiles = response.data;
      console.log(response.data);
      setBidProfiles(profiles);
    });
  };

  useEffect(() => {
    getBidProfiles();
  }, []);

  return (
    <>
      <Layout title="Bid Profile" />
      <Grid container className={classes.main}>
        <Typography variant="h2">Bid Profile</Typography>
      </Grid>
      <Grid container></Grid>
    </>
  );
};

export default Profile;
