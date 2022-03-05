import React from "react";
import useStyles from "../../utils/styles";
import { Button, FormControl, FormGroup, FormLabel } from "@material-ui/core";
import { Select } from "@material-ui/core";
import { MenuItem } from "@material-ui/core";
import { Input } from "@material-ui/core";
import { useState } from "react";
import axios from "axios";

const AccountUploadForm = () => {
  const classes = useStyles();
  const [account, setAccount] = useState("");
  const [file, setFile] = useState(null);

  const accounts = [
    {
      name: "Juvo Amazon US",
      account: "Juvo_AMZUS",
      salesChannelId: 1111,
    },
    {
      name: "Talented Kitchen Amazon US",
      account: "TLK_AMZUS",
      salesChannelId: 1141,
    },
    {
      name: "Juvo Amazon Canada",
      account: "Juvo_AMZCA",
      salesChannelId: 1121,
    },
  ];
  const handleSelectOnChange = (e) => {
    const value = e.target.value;
    setAccount(value);
    console.log(value);
  };

  const handleFileOnChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    const url = "http://localhost:8000/utility/iso_keyword/";
    e.preventDefault();
    const formData = new FormData();
    console.log(account);
    console.log(file);

    // const header =
    formData.append("account", account);
    formData.append("file", file);
    axios
      .post(url, formData, {
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

  return (
    <>
      <FormGroup className={classes.formGroup}>
        <FormLabel id="account-label">Account</FormLabel>
        <Select
          // variant="outlined"
          defaultValue={accounts ? accounts[0]["account"] : ""}
          labelId="account-label"
          value={account}
          onChange={handleSelectOnChange}
          autoFocus
          className={classes.formElement}
        >
          {accounts.map((item, index) => {
            return (
              <MenuItem key={index} value={item.account}>
                {`${item.name} - ${item.salesChannelId}`}
              </MenuItem>
            );
          })}
        </Select>
        <Input
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
          onClick={handleSubmit}
        >
          Submit
        </Button>
      </FormGroup>
    </>
  );
};

export default AccountUploadForm;
