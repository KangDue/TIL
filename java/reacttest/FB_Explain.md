- The code imports three functions, ref, set, child, and get from the Firebase Database module.

1. ref creates a reference to a specific location in the Firebase Real-time Database. It takes a path string as an argument and returns a database reference that points to that path in the database.

2. set is used to write data to the database. It takes two arguments: the reference to the location in the database where you want to set the data, and the new data you want to set.

3. child is used to access a child location in the database. It takes the path of the child location as an argument and returns a reference to that child location. This is useful when you need to access a specific sub-path within the database.

4. get is used to retrieve data from the database. It takes a reference to the location in the database from which you want to retrieve data as an argument and returns the data stored at that location.

<hr>

useState is a hook in React that allows you to add state to functional components. State is an object that holds data that can change during the lifetime of a component and affects the rendering of a component.

useState returns an array with two elements: the first element is the current state value, and the second is a function to update it. You can call the update function to change the state value.

In the code you provided, const [todo, setTodo] = useState(""); creates a state variable named todo with an initial value of an empty string and a function setTodo to update its value. The handleTodoChange function updates the value of todo by calling setTodo with the new value.

- <Strong>conclusion</Strong>
UseState("") initialize todo's value equal to "" and define setTodo Function who's parameter is todo.

<br>
[파이어베이스 쿼리](https://m.blog.naver.com/zoown13/222094002924)
[파이어베이스 배열](https://firebase.blog/posts/2014/04/best-practices-arrays-in-firebase)

<br>
- 특정 코드 설명
```
ref.on('value', function(snap) { list = snap.val(); });
```
a Firebase Realtime Database event listener that listens for changes in the data stored at the location pointed to by the ref variable.

ref.on('value', ...): The on method is used to attach an event listener in the Firebase Realtime Database. It listens for changes in the data stored at the location pointed to by the ref variable. The first argument to on is the event type to listen to, in this case it's "value".

function(snap) {...}: This is the callback function that gets called every time the data stored at the location pointed to by the ref variable changes. The snap argument is a DataSnapshot object that represents the data at the location at the time the event was triggered.

list = snap.val(): The snap.val() method retrieves the value of the data stored at the location pointed to by the ref variable. In this code, it updates the list array with the new data.

The "on" method in Firebase Realtime Database provides a real-time event listener for a specified database reference. It listens for changes in the database and triggers the associated callback function when the data changes.

Here are some of the event types that you can use with the "on" method:

1. value: This type listens for changes in the entire data at the specified reference.

2. child_added: This type listens for the addition of a new child node to the specified reference.

3. child_changed: This type listens for changes to the data of an existing child node at the specified reference.

4. child_removed: This type listens for the removal of a child node from the specified reference.

5. child_moved: This type listens for changes to the order of child nodes at the specified reference.

You can use these event types to get notified of changes in the Firebase Realtime Database and take action based on the changes.

<hr>























<hr>
<hr>
<hr>
[리액트 시작하기](https://chanhuiseok.github.io/posts/react-2/)