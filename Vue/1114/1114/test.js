
async function go() {
  const a = await setTimeout(()=>{resolve(console.log(1))},1000)
  console.log(2)
}
go()