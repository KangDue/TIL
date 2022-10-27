const forms = document.querySelectorAll('.like-form')
// 이런식으로 가능
// document.querySelector('form[data-article-id="2"]')  
forms.forEach((form) => { 
  let form_id = form.getAttribute('data-article-id')
  console.log(form_id)
  form.addEventListener('submit',function (event) {
    event.preventDefault()
    console.log(event)
  })
 })