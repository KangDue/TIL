// 코드를 작성해 주세요
let p1 = document.querySelector('#player1-img')
let p2 = document.querySelector('#player2-img')
let choice = document.querySelector('section')
//querySelector('img').src
// console.log("before");
// setTimeout(() => console.log("after"), 3000);
//가위 0, 바위 1, 보 2
let result = {
  0:2,
  1:0,
  2:1,
}

let code = {
  'scissors':0,
  'rock':1,
  'paper':2,
}

function tog1() {
  choice.children[0].toggleAttribute('disabled')
  choice.children[0].style = 'background-color:red'
  choice.children[1].toggleAttribute('disabled')
  choice.children[1].style = 'background-color:red'
  choice.children[2].toggleAttribute('disabled')
  choice.children[2].style = 'background-color:red'
  for (let j=0;j<30;j++){
    setTimeout(() => {
      computer = _.sample([0,1,2])
      p2.src = choice.children[computer].querySelector('img').src
    },100)}
}
function tog2(event) {
  p2.src = choice.children[computer].querySelector('img').src
  for (let i in code){
    if (p1.src.search(i) > 0){
      var temp = code[i]
      break
    }
  }
  modal_content.innerText = rcp(1,temp)
  modal.style.display = 'block'
  choice.children[0].toggleAttribute('disabled')
  choice.children[0].style = ''
  choice.children[1].toggleAttribute('disabled')
  choice.children[1].style = ''
  choice.children[2].toggleAttribute('disabled')
  choice.children[2].style = ''
}



function rcp(a,b) {
  console.log(a,b)
  if (result[a] === b){
    return 'Player1 win'
  }
  else if (a === b){
    return 'Draw'
  }
  else {
    return 'Computer Win'
  }
}


let modal = document.querySelector('.modal')
let modal_content = document.querySelector('.modal-content')

let computer = 0
let sci = choice.children[0]
let rock = choice.children[1]
let paper = choice.children[2]
sci.setAttribute('num',0)
rock.setAttribute('num',1)
paper.setAttribute('num',2)

for (let i=0;i<3;i++){
  choice.children[i].addEventListener('click',function(event){
    p1.src = choice.children[i].querySelector('img').src

    tog1()
    setTimeout(tog2, 3000);
    }
    )
  }
modal.addEventListener('click',function(event) {
  modal.style.display = 'none'
})

