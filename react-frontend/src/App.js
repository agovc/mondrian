import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  class Square extends React.Component {
    render() {
      var squareStyle = {
        margin: 5,
        width: "100%",
        float: "left",
        backgroundColor: this.props.bgColor,
        height: this.props.sqHeight
      };
      return (
        <div style={squareStyle}>
        </div>
      );
    }
  }

  function MondrianOne(props) {
    return(
      <div className="container-one">
        <div className="one-one">
          <Square bgColor={window.a} sqHeight="80px" />
          <Square bgColor={window.b} sqHeight="130px" />
        </div>
        <div className="two-one">
          <Square bgColor={window.c} sqHeight="220px" />
        </div>
        <div className="three-one">
          <Square bgColor={window.d} sqHeight="30px" />
          <Square bgColor={window.e} sqHeight="120px" />
          <Square bgColor={window.f} sqHeight="50px" />
        </div>
      </div>
    );
  }

  function MondrianTwo(props) {
    return(
      <div className="container-two">
        <div className="one-two">
          <Square bgColor={window.d} sqHeight="100px" />
          <Square bgColor={window.e} sqHeight="160px" />
          <Square bgColor={window.f} sqHeight="50px" />
        </div>
        <div className="two-two">
          <Square bgColor={window.c} sqHeight="330px" />
        </div>
        <div className="three-two">
          <Square bgColor={window.a} sqHeight="50px" />
          <Square bgColor={window.b} sqHeight="270px" />
        </div>
      </div>
    );
  }

  function Mondrian(props) {
    const rand = Boolean(Math.round(Math.random()));

    if (rand) {
      return <MondrianOne />;
    }
    return <MondrianTwo />;
  }

  return (
    <div className="App">
      <header className="App-header">
        <p className="righteous">{window.name}</p>
        <p className="author">BY @AGOVC</p>

        <Mondrian />

      </header>

    </div>

  );
}

export default App;
