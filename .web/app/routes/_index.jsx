import {Fragment,useCallback,useContext,useEffect} from "react"
import {Button as RadixThemesButton,Flex as RadixThemesFlex,Heading as RadixThemesHeading,Spinner as RadixThemesSpinner} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isTrue} from "$/utils/state"
import {jsx} from "@emotion/react"




function Button_0d683f5b0832c33dc8a05bf3475a4d56 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_9ca09a608fc72a1f52ec597d6e076be2 = useCallback(((_e) => (addEvents([(ReflexEvent("_redirect", ({ ["path"] : "/chat", ["external"] : false, ["popup"] : false, ["replace"] : false }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["width"] : "100%" }),onClick:on_click_9ca09a608fc72a1f52ec597d6e076be2},"go to the chat")
  )
}


function Fragment_9bd3cc625420aea66164eeeee859c215 () {
  const reflex___state____state__reflex_proj___reflex_proj____state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____state)



  return (
    jsx(Fragment,{},(reflex___state____state__reflex_proj___reflex_proj____state.finished_training_rx_state_?(jsx(Fragment,{},jsx(Button_0d683f5b0832c33dc8a05bf3475a4d56,{},))):(jsx(Fragment,{},))))
  )
}


function Flex_c9c1b95467f8217f5519a2f1214f7249 () {
  
                useEffect(() => {
                    ((...args) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____state.train_model", ({  }), ({  })))], args, ({  }))))()
                    return () => {
                        
                    }
                }, []);
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%", ["height"] : "100vh" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesHeading,{css:({ ["fontSize"] : "1.5em" })},"Loading model"),jsx(RadixThemesSpinner,{size:"3"},)),jsx(Fragment_9bd3cc625420aea66164eeeee859c215,{},)))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(Flex_c9c1b95467f8217f5519a2f1214f7249,{},),jsx("title",{},"ReflexProj | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}