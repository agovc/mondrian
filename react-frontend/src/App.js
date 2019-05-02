import React from 'react';
import logo from './logo.svg';
import $ from 'jquery';
import './App.css';

function App() {

  class Square extends React.Component {
    render() {
      var squareStyle = {
        margin: 5,
        width: this.props.sqWidth,
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
      <div className="container-one painting">
        <div className="columnStyle">
          <Square bgColor={window.a} sqHeight={window.r1_1} sqWidth={window.p_w1_1} />
          <Square bgColor={window.b} sqHeight={window.c1_1} sqWidth={window.p_w1_1} />
        </div>
        <div className="columnStyle">
          <Square bgColor={window.c} sqHeight="220px" sqWidth={window.p_w2_1} />
        </div>
        <div className="columnStyle">
          <Square bgColor={window.d} sqHeight={window.r2_1} sqWidth={window.p_w3_1} />
          <Square bgColor={window.e} sqHeight={window.r3_1} sqWidth={window.p_w3_1} />
          <Square bgColor={window.f} sqHeight={window.c2_1} sqWidth={window.p_w3_1} />
        </div>
      </div>
    );
  }

  function MondrianTwo(props) {
    return(
      <div className="container-two painting">
        <div className="columnStyle">
          <Square bgColor={window.d} sqHeight={window.r1_2} sqWidth={window.p_w1_2} />
          <Square bgColor={window.e} sqHeight={window.r2_2} sqWidth={window.p_w1_2} />
          <Square bgColor={window.f} sqHeight={window.r3_2} sqWidth={window.p_w1_2} />
        </div>
        <div className="columnStyle">
          <Square bgColor={window.c} sqHeight="330px" sqWidth={window.p_w2_2} />
        </div>
        <div className="columnStyle">
          <Square bgColor={window.a} sqHeight={window.r4_2} sqWidth={window.p_w3_2} />
          <Square bgColor={window.b} sqHeight={window.r5_2} sqWidth={window.p_w3_2} />
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

  function refreshPage(){
    window.location.reload();
  }

  return (
    <div className="App">
      <header className="App-header">
        <p className="righteous">{window.name}</p>
        <p className="author">w/ 💕 by @AGOVC, about <a target="_blank" href="https://github.com/agovc/mondrian">the PROJECT</a></p>

        <button className="button" type="button" onClick={ refreshPage }>
        <Mondrian />
        </button>

      </header>



    </div>

  );

}

export default App;
