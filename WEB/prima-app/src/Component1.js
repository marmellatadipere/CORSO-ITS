import React from 'react'

const Component1 = (props) => {
  console.log(props);
  return (
    <div>Component1 di {props.children}</div>
  )
}

export default Component1