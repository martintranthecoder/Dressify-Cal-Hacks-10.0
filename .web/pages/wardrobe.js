import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import range from "/utils/helpers/range.js"
import "focus-visible/dist/focus-visible"
import { Button, Center, Image, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, SimpleGrid, Stack, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Center sx={{"background": "linear-gradient(180deg, #050303 0%, #2D2E2E 100%)"}}>
  <VStack alignItems={`center`} justifyContent={`center`} sx={{"display": "flex", "height": "100vh"}}>
  <Button onClick={(_e) => addEvents([Event("_redirect", {path:`/`,external:false})], (_e), {})} size={`md`} sx={{"color": "#BCABAE"}}>
  {`HOME`}
</Button>
  <Text sx={{"color": "#FBFBFB", "fontFamily": "static/Raleway-Light.ttf", "fontSize": "2em", "fontStyle": "normal", "fontWeight": "400", "lineHeight": "normal", "bottom": "120px", "position": "relative", "paddingTop": "0%"}}>
  {`Wardrobe`}
</Text>
  <SimpleGrid columns={[3]} spacing={`10`} sx={{"margin": "auto"}}>
  {state.wardrobe_state.image_urls.map((iktadvlk, zxyleqvp) => (
  <Text key={zxyleqvp}>
  <Image src={iktadvlk}/>
</Text>
))}
</SimpleGrid>
  <Stack direction={`column`}>
  <Button onClick={(_e) => addEvents([Event("_redirect", {path:`/selections`,external:false})], (_e), {})} size={`md`} sx={{"color": "#BCABAE", "border": "10%"}}>
  {`ADD MORE`}
</Button>
  <Button onClick={(_e) => addEvents([Event("_redirect", {path:`/results`,external:false})], (_e), {})} size={`md`} sx={{"color": "#BCABAE"}}>
  {`GENERATE`}
</Button>
</Stack>
</VStack>
</Center>
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
