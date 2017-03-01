

// 127.0.0.1:8000

//let base = 'http://127.0.0.1:8000';

let base = 'http://123.206.113.243';

export const getGithub = params => { return axios.get(`${base}/api/github/day`, { params: params }); };

export const getHackerNews = params => { return axios.get(`${base}/api/hackernews`, { params: params }); };

export const getGank = params => { return axios.get(`http://gank.io/api/random/data/all/20`, { params: params }); };

// export const getGank = params => { return axios.get(`${base}/api/gank`, { params: params }); };



