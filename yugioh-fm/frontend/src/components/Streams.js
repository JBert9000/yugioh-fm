import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class Streams extends Component {
  render() {
    return <h1>If you're seeing this, Streams Component is imported. Test Test Test</h1>
  }
};

ReactDOM.render(<Streams />, document.getElementById('streams'));
