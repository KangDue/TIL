/* 
  아래에 코드를 작성해주세요.
*/
let keyword
let searchBtn = document.querySelector('.search-box__button')
let albums

let div1 = document.createElement('div')
div1.classList.add('search-result__card')
let img1 = document.createElement('img')
img1.setAttribute('src','')
let div2 = document.createElement('div')
div2.classList.add('search-result__text')
let h2 = document.createElement('h2')
let p = document.createElement('p')
div2.append(h2,p)
div1.append(img1,div2)

let copy_div = div1.cloneNode(1)

function fetchAlbums(page=1,limit=10) {
  let my_api_key = '7ad65284e3bec41aef2867db61d82ec7'
  let ax = axios({
    method:'get',
    url:`http://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword}&api_key=${my_api_key}&format=json&page=${page}&limit=${limit}`
  })
  .then((request) => {
    albums = request.data.results.albummatches.album
    return request
  })
  .then((request)=> {
    albums.forEach((val,key) => {
      let item = copy_div.cloneNode(1)
      item.querySelector('img').src = val.image[1]['#text']
      item.querySelector('h2').innerText = val.artist
      item.querySelector('p').innerText = val.name
      // console.log(val.name)
      // console.log(val.artist)
      // console.log(val.url)
      document.body.appendChild(item)
    })
    return request
  })
  .catch((request) => {
    console.log(request)
    alert('잠시후 다시 시도해 주세요')
    return request
  })
  return ax
}

document.querySelector('input').addEventListener('keydown',(event) => {
  if (event.key === 'Enter') {
    searchBtn.click()
  }
  })

let page_num = 1
searchBtn.addEventListener('click',function(event) {
  keyword = document.querySelector('.search-box__input').value
  fetchAlbums(1)

  function moreInfo(e) {
    if (window.scrollY + window.innerHeight >= document.body.scrollHeight ){
      fetchAlbums(++page_num,limit=10)
    }
  }
  window.addEventListener('scroll',moreInfo)

})