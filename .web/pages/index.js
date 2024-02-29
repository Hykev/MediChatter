/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, getBackendURL, isTrue, set_val } from "/utils/state"
import { Box as RadixThemesBox, Button as RadixThemesButton, Container as RadixThemesContainer, Dialog as RadixThemesDialog, Flex as RadixThemesFlex, Text as RadixThemesText, Theme as RadixThemesTheme } from "@radix-ui/themes"
import env from "/env.json"
import "@radix-ui/themes/styles.css"
import theme from "/utils/theme.js"
import { Input } from "@chakra-ui/react"
import NextHead from "next/head"



export function Button_9e74c513f3a981afc174c34b40ccd4ac () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_f4ecaeca7ac4803e870637fe18cb1eea = useCallback((_e) => addEvents([Event("state.state.answer", {})], (_e), {}), [addEvents, Event])

  return (
    <RadixThemesButton css={{"backgroundColor": "green", "boxShadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px", "size": "3"}} onClick={on_click_f4ecaeca7ac4803e870637fe18cb1eea}>
  {`Consultar`}
</RadixThemesButton>
  )
}

export function Fragment_1762bb90abdb81b879b2a22edbbe01a1 () {
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <RadixThemesDialog.Root open={connectError !== null}>
  <RadixThemesDialog.Content>
  <RadixThemesDialog.Title>
  {`Connection Error`}
</RadixThemesDialog.Title>
  <RadixThemesText as={`p`}>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getBackendURL(env.EVENT).href}
</RadixThemesText>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Box_9b47f911424a76abcaa12374902a0ce3 () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <RadixThemesBox>
  {state__state.chat_history.map((messages, index_ab81cf08a1fd2aef01760868b8641e1a) => (
  <RadixThemesBox css={{"marginTop": "1em", "marginBottom": "1em"}} key={index_ab81cf08a1fd2aef01760868b8641e1a}>
  <RadixThemesBox css={{"textAlign": "right"}}>
  <RadixThemesText as={`p`} css={{"padding": "1em", "borderRadius": "5px", "marginTop": "0.5em", "marginBottom": "0.5em", "boxShadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px", "maxWidth": "30em", "display": "inline-block", "background": "#50e1e6", "marginLeft": "20%"}}>
  {messages.at(0)}
</RadixThemesText>
</RadixThemesBox>
  <RadixThemesBox css={{"textAlign": "left"}}>
  <RadixThemesText as={`p`} css={{"padding": "1em", "borderRadius": "5px", "marginTop": "0.5em", "marginBottom": "0.5em", "boxShadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px", "maxWidth": "30em", "display": "inline-block", "marginRight": "20%"}}>
  {messages.at(1)}
</RadixThemesText>
</RadixThemesBox>
</RadixThemesBox>
))}
</RadixThemesBox>
  )
}

export function Input_dcacf799b9bbc265684081bae1a690fe () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_change_c1fe93b939c866e1de40fb642568d5e0 = useCallback((_e0) => addEvents([Event("state.state.set_question", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <Input onChange={on_change_c1fe93b939c866e1de40fb642568d5e0} placeholder={`Escribe tu síntoma`} sx={{"borderWidth": "1px", "padding": "1em", "boxShadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px"}}/>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_1762bb90abdb81b879b2a22edbbe01a1/>
  <RadixThemesContainer>
  <Box_9b47f911424a76abcaa12374902a0ce3/>
  <RadixThemesFlex align={`start`} direction={`row`} gap={`2`}>
  <Input_dcacf799b9bbc265684081bae1a690fe/>
  <Button_9e74c513f3a981afc174c34b40ccd4ac/>
</RadixThemesFlex>
</RadixThemesContainer>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
