'use strict';

function Homepage() {

  return (
    <div>
      <h1>Welcome!</h1>
      <p><a href="/cards">Go to the Cards Page</a></p>
      <img src="/static/img/balloonicorn.jpg"/>

      <p><a href="/about">Go the the About Page</a></p>
    </div>
  );
}

ReactDOM.render(<Homepage />, document.querySelector('#app'));
