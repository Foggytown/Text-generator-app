import {Fragment,useCallback,useContext,useEffect} from "react"
import {Button as RadixThemesButton,Flex as RadixThemesFlex,Heading as RadixThemesHeading,Spinner as RadixThemesSpinner} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isTrue} from "$/utils/state"
import {jsx} from "@emotion/react"




function Fragment_90651842a1eb0d0b5626b8432e572c76 () {
  const reflex___state____state__reflex_proj___reflex_proj____state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____state)



  return (
    jsx(Fragment,{},(reflex___state____state__reflex_proj___reflex_proj____state.loading_rx_state_?(jsx(Fragment,{},jsx(RadixThemesSpinner,{size:"3"},))):(jsx(Fragment,{},))))
  )
}


function Button_159ebd13a051012d965cf803cd0da215 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_2c6c9bd09c7090e279e13cb69db6787b = useCallback(((_e) => (addEvents([(ReflexEvent("_redirect", ({ ["path"] : "/email", ["external"] : false, ["popup"] : false, ["replace"] : false }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["width"] : "100%" }),onClick:on_click_2c6c9bd09c7090e279e13cb69db6787b},"go to the chat")
  )
}


function Fragment_0ab7891d2c4796dad591aa7b2028f012 () {
  const reflex___state____state__reflex_proj___reflex_proj____state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____state)



  return (
    jsx(Fragment,{},(reflex___state____state__reflex_proj___reflex_proj____state.finished_loading_rx_state_?(jsx(Fragment,{},jsx(Button_159ebd13a051012d965cf803cd0da215,{},))):(jsx(Fragment,{},))))
  )
}


function Flex_550776ef434f649aec3255421e761c07 () {
  
                useEffect(() => {
                    ((...args) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____state.load_model", ({  }), ({  })))], args, ({  }))))()
                    return () => {
                        
                    }
                }, []);
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%", ["height"] : "100vh" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesHeading,{css:({ ["fontSize"] : "1.5em" })},"Loading model"),jsx(Fragment_90651842a1eb0d0b5626b8432e572c76,{},)),jsx(Fragment_0ab7891d2c4796dad591aa7b2028f012,{},)))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(Flex_550776ef434f649aec3255421e761c07,{},),jsx("title",{},"ReflexProj | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}