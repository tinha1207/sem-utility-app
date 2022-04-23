import React from "react";
import useStyles from "../../utils/styles";
import { Button, FormControl, FormGroup, FormLabel } from "@material-ui/core";
import { Select } from "@material-ui/core";
import { MenuItem } from "@material-ui/core";
import { Input } from "@material-ui/core";
import { useState, useEffect } from "react";
import axios from "axios";

const AccountUploadForm = () => {
  const classes = useStyles();
  const [prefix, setPrefix] = useState("");
  const [file, setFile] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const accountUrl = "http://localhost:8002/account/";
  const isoKeywordUrl = "http://localhost:8001/utility/iso_keyword/";

  const handleSelectOnChange = (e) => {
    const value = e.target.value;
    setPrefix(value);
    console.log(value);
  };

  const handleFileOnChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    let formData = new FormData();
    formData.append("account", prefix);
    formData.append("file", file);
    axios
      .post(isoKeywordUrl, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
        responseType: "arraybuffer",
      })
      .then((response) => {
        const tempUrl = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = tempUrl;
        link.setAttribute("Download", "file.xlsx");
        document.body.appendChild(link);
        link.click();
      });
  };

  useEffect(() => {
    axios.get(accountUrl).then((response) => {
      setAccounts(response.data);
    });
  }, []);

  return (
    <>
      <form onSubmit={handleSubmit}>
        <FormGroup className={classes.formGroup}>
          <FormLabel id="account-input-label">Account</FormLabel>
          <Select
            labelId="account-input-label"
            value={prefix}
            onChange={handleSelectOnChange}
            autoFocus
            className={classes.formElement}
          >
            {accounts.map((item) => {
              return (
                <MenuItem key={item.id} value={item.campaign_prefix}>
                  {`${item.name} - ${item.sales_channel_id}`}
                </MenuItem>
              );
            })}
          </Select>
          <FormLabel id="file-input-label">ISO File Upload</FormLabel>
          <Input
            labelId="file-input-label"
            id="file-upload"
            type="file"
            className={classes.formElement}
            onChange={handleFileOnChange}
          ></Input>
          <Button
            className={classes.formElement}
            type="submit"
            variant="contained"
            color="primary"
            size="small"
            // onClick={handleSubmit}
          >
            Submit
          </Button>
        </FormGroup>
      </form>
    </>
  );
};

export default AccountUploadForm;
