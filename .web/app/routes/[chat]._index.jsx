import {Fragment,useCallback,useContext,useEffect} from "react"
import {Button as RadixThemesButton,Flex as RadixThemesFlex,Heading as RadixThemesHeading,Text as RadixThemesText,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isTrue} from "$/utils/state"
import {jsx} from "@emotion/react"




function Textfield__root_44144875aedf8ac91713d0c81141e1a3 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_blur_3ab054657fa23e1d72cc399f73094ab1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____state.set_prompt", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesTextField.Root,{css:({ ["width"] : "25em" }),onBlur:on_blur_3ab054657fa23e1d72cc399f73094ab1,placeholder:"Enter a prompt.."},)
  )
}


function Textfield__root_16126d4f830cff2c3a64914bbff6d9ff () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_blur_b3090292899a53a1bcc6680eb3ba6a6b = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____state.set_num_words", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesTextField.Root,{css:({ ["width"] : "25em" }),onBlur:on_blur_b3090292899a53a1bcc6680eb3ba6a6b,placeholder:"Enter how many words to generate"},)
  )
}


function Button_c90d573a96e5df0054ef107324d7e0a6 () {
  const reflex___state____state__reflex_proj___reflex_proj____state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_48b301b6b4a5626f9ae8153cc08d6fc5 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____state.get_new_words", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["width"] : "25em" }),loading:reflex___state____state__reflex_proj___reflex_proj____state.processing_rx_state_,onClick:on_click_48b301b6b4a5626f9ae8153cc08d6fc5},"Generate new words")
  )
}


function Text_1b3efb74e8565a5082f818caef91d238 () {
  const reflex___state____state__reflex_proj___reflex_proj____state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____state)



  return (
    jsx(RadixThemesText,{as:"p"},reflex___state____state__reflex_proj___reflex_proj____state.result_rx_state_)
  )
}


function Fragment_0880ecd3295cf51e756a331ace7ddc0e () {
  const reflex___state____state__reflex_proj___reflex_proj____state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____state)



  return (
    jsx(Fragment,{},(reflex___state____state__reflex_proj___reflex_proj____state.complete_rx_state_?(jsx(Fragment,{},jsx(Text_1b3efb74e8565a5082f818caef91d238,{},))):(jsx(Fragment,{},))))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%", ["height"] : "100vh" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"column",gap:"3"},jsx(RadixThemesHeading,{css:({ ["fontSize"] : "1.5em" })},"n-gram generation"),jsx(Textfield__root_44144875aedf8ac91713d0c81141e1a3,{},),jsx(Textfield__root_16126d4f830cff2c3a64914bbff6d9ff,{},),jsx(Button_c90d573a96e5df0054ef107324d7e0a6,{},),jsx(Fragment_0880ecd3295cf51e756a331ace7ddc0e,{},))),jsx("title",{},"ReflexProj | Chat"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}