import os
import axios from 'axios';

let api = axios.create({
    headers: {
      'Client-ID': os.environ.get("TWITCH_API_KEY")
    }
})

export default api;
