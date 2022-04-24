//使用していない
import Axios from "axios";
//import Cookies from "js-cookie";
const axios = Axios.create({
    baseURL: process.env.VUE_APP_BASEURL,
    timeout: 2500,
    headers: {
        Authorization: `JWT ${this.$session.get("token")}`,
    },
});