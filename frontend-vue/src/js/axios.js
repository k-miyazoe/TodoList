import Axios from "axios";
import Cookies from "js-cookie";

function set_header(jwt) {
    const csrftoken = Cookies.get("csrftoken");
    //console.log('env check', process.env, jwt)
    let axios = Axios.create({
        baseURL: process.env.VUE_APP_API_URL,
        timeout: 2500,
        headers: {
            "Content-Type": "application/json",
            Authorization: jwt,
            "X-CSRFToken": csrftoken,
        },
    });
    return axios
}

//関数をexport
export default {
    set_header,
};