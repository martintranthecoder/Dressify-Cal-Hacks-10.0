import { Fragment, useCallback, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import range from "/utils/helpers/range.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Center, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, option, Select, Text, VStack } from "@chakra-ui/react"
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

  const ref_itemtype = useRef(null); refs['ref_itemtype'] = ref_itemtype;
  const ref_color = useRef(null); refs['ref_color'] = ref_color;
  const ref_secondaryattribute = useRef(null); refs['ref_secondaryattribute'] = ref_secondaryattribute;
  const ref_primaryattribute = useRef(null); refs['ref_primaryattribute'] = ref_primaryattribute;
  const ref_gender = useRef(null); refs['ref_gender'] = ref_gender;
  const ref_season = useRef(null); refs['ref_season'] = ref_season;
  
    const handleSubmitmwqnixqq = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{"season": getRefValue(ref_season), "gender": getRefValue(ref_gender), "secondaryattribute": getRefValue(ref_secondaryattribute), "primaryattribute": getRefValue(ref_primaryattribute), "color": getRefValue(ref_color), "itemtype": getRefValue(ref_itemtype)}}

        addEvents([Event("state.wardrobe_state.handle_form", {form_data:form_data})])

        if (false) {
            $form.reset()
        }
    })
    

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
  <Center>
  <VStack spacing={`1.5em`} sx={{"textAlign": "center", "fontSize": "2em", "paddingTop": "10%", "height": "100vh", "paddingBottom": "10%"}}>
  <Button onClick={(_e) => addEvents([Event("_redirect", {path:`/`,external:false})], (_e), {})} size={`md`} sx={{"color": "#BCABAE"}}>
  {`HOME`}
</Button>
  <Text sx={{"color": "#FBFBFB", "fontSize": "2em", "fontFamily": "static/Raleway-Light.ttf", "fontWeight": 400, "wordWrap": "break-word"}}>
  {`Selections`}
</Text>
  <Text sx={{"width": "100%", "height": "100%", "color": "#FBFBFB", "fontSize": "1em", "fontFamily": "static/Raleway-Light.ttf", "fontWeight": 400, "wordWrap": "break-word", "display": "flex", "justifyContent": "center", "alignItems": "center"}}>
  {`Let's Start by Filtering Your Selection!`}
</Text>
  <Box as={`form`} onSubmit={handleSubmitmwqnixqq}>
  <Select id={`gender`} placeholder={`Select a gender.`} ref={ref_gender} size={`lg`}>
  <option value={`women`}>
  {`women`}
</option>
  <option value={`men`}>
  {`men`}
</option>
  <option value={`unisex`}>
  {`unisex`}
</option>
</Select>
  <Select id={`primaryattribute`} placeholder={`Select a primary attribute.`} ref={ref_primaryattribute} size={`lg`}>
  <option value={`apparel`}>
  {`apparel`}
</option>
  <option value={`accessories`}>
  {`accessories`}
</option>
  <option value={`footwear`}>
  {`footwear`}
</option>
</Select>
  <Select id={`secondaryattribute`} placeholder={`Select a secondary attribute.`} ref={ref_secondaryattribute} size={`lg`}>
  <option value={`topwear`}>
  {`topwear`}
</option>
  <option value={`bottomwear`}>
  {`bottomwear`}
</option>
  <option value={`shoes`}>
  {`shoes`}
</option>
  <option value={`jewelry`}>
  {`jewelry`}
</option>
  <option value={`eyewear`}>
  {`eyewear`}
</option>
  <option value={`dress`}>
  {`dress`}
</option>
  <option value={`accessories`}>
  {`accessories`}
</option>
</Select>
  <Select id={`itemtype`} placeholder={`Select an item type.`} ref={ref_itemtype} size={`lg`}>
  <option value={`shirts`}>
  {`shirts`}
</option>
  <option value={`jeans`}>
  {`jeans`}
</option>
  <option value={`track pants`}>
  {`track pants`}
</option>
  <option value={`casual shoes`}>
  {`casual shoes`}
</option>
  <option value={`tops`}>
  {`tops`}
</option>
  <option value={`sweatshirts`}>
  {`sweatshirts`}
</option>
  <option value={`formal shoes`}>
  {`formal shoes`}
</option>
  <option value={`bracelet`}>
  {`bracelet`}
</option>
  <option value={`flats`}>
  {`flats`}
</option>
  <option value={`waistcoat`}>
  {`waistcoat`}
</option>
  <option value={`sports shoes`}>
  {`sports shoes`}
</option>
  <option value={`shorts`}>
  {`shorts`}
</option>
  <option value={`heels`}>
  {`heels`}
</option>
  <option value={`saree`}>
  {`saree`}
</option>
  <option value={`sunglasses`}>
  {`sunglasses`}
</option>
  <option value={`scarves`}>
  {`scarves`}
</option>
  <option value={`dresses`}>
  {`dresses`}
</option>
  <option value={`skirts`}>
  {`skirts`}
</option>
  <option value={`blazers`}>
  {`blazers`}
</option>
  <option value={`ring`}>
  {`ring`}
</option>
  <option value={`caps`}>
  {`caps`}
</option>
  <option value={`trousers`}>
  {`trousers`}
</option>
  <option value={`earrings`}>
  {`earrings`}
</option>
  <option value={`camisoles`}>
  {`camisoles`}
</option>
  <option value={`tunics`}>
  {`tunics`}
</option>
  <option value={`jackets`}>
  {`jackets`}
</option>
  <option value={`necklace and chains`}>
  {`necklace and chains`}
</option>
  <option value={`sweaters`}>
  {`sweaters`}
</option>
</Select>
  <Select id={`color`} placeholder={`Select a color.`} ref={ref_color} size={`lg`}>
  <option value={`navy blue`}>
  {`navy blue`}
</option>
  <option value={`blue`}>
  {`blue`}
</option>
  <option value={`black`}>
  {`black`}
</option>
  <option value={`grey`}>
  {`grey`}
</option>
  <option value={`green`}>
  {`green`}
</option>
  <option value={`purple`}>
  {`purple`}
</option>
  <option value={`white`}>
  {`white`}
</option>
  <option value={`beige`}>
  {`beige`}
</option>
  <option value={`brown`}>
  {`brown`}
</option>
  <option value={`bronze`}>
  {`bronze`}
</option>
  <option value={`teal`}>
  {`teal`}
</option>
  <option value={`copper`}>
  {`copper`}
</option>
  <option value={`pink`}>
  {`pink`}
</option>
  <option value={`off white`}>
  {`off white`}
</option>
  <option value={`maroon`}>
  {`maroon`}
</option>
  <option value={`red`}>
  {`red`}
</option>
  <option value={`khaki`}>
  {`khaki`}
</option>
  <option value={`orange`}>
  {`orange`}
</option>
  <option value={`coffee brown`}>
  {`coffee brown`}
</option>
  <option value={`yellow`}>
  {`yellow`}
</option>
  <option value={`charcoal`}>
  {`charcoal`}
</option>
  <option value={`gold`}>
  {`gold`}
</option>
  <option value={`steel`}>
  {`steel`}
</option>
  <option value={`tan`}>
  {`tan`}
</option>
  <option value={`multi`}>
  {`multi`}
</option>
  <option value={`magenta`}>
  {`magenta`}
</option>
  <option value={`lavender`}>
  {`lavender`}
</option>
  <option value={`sea green`}>
  {`sea green`}
</option>
  <option value={`cream`}>
  {`cream`}
</option>
  <option value={`peach`}>
  {`peach`}
</option>
  <option value={`olive`}>
  {`olive`}
</option>
  <option value={`skin`}>
  {`skin`}
</option>
  <option value={`burgundy`}>
  {`burgundy`}
</option>
  <option value={`grey melange`}>
  {`grey melange`}
</option>
  <option value={`rust`}>
  {`rust`}
</option>
  <option value={`rose`}>
  {`rose`}
</option>
  <option value={`lime green`}>
  {`lime green`}
</option>
  <option value={`mauve`}>
  {`mauve`}
</option>
  <option value={`turquoise`}>
  {`turquoise`}
</option>
  <option value={`metallic`}>
  {`metallic`}
</option>
  <option value={`mustard`}>
  {`mustard`}
</option>
  <option value={`taupe`}>
  {`taupe`}
</option>
  <option value={`nude`}>
  {`nude`}
</option>
  <option value={`mushroom`}>
  {`mushroom`}
</option>
  <option value={`fluorescence`}>
  {`fluorescence`}
</option>
</Select>
  <Select id={`season`} placeholder={`Select a season.`} ref={ref_season} size={`lg`}>
  <option value={`fall`}>
  {`fall`}
</option>
  <option value={`summer`}>
  {`summer`}
</option>
  <option value={`winter`}>
  {`winter`}
</option>
  <option value={`spring`}>
  {`spring`}
</option>
</Select>
  <Button onClick={(_e) => addEvents([Event("_redirect", {path:`/results`,external:false})], (_e), {})} sx={{"border": "0.1em solid", "padding": "0.5em", "borderRadius": "0.5em", "Hover": {"color": isTrue((colorMode === "light")) ? `rgb(107,99,246)` : `rgb(179, 175, 255)`}}} type={`submit`}>
  {`GENERATE`}
</Button>
</Box>
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
