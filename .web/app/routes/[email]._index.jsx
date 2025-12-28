import {Fragment,useCallback,useContext,useEffect} from "react"
import {Box as RadixThemesBox,Button as RadixThemesButton,Card as RadixThemesCard,Flex as RadixThemesFlex,Heading as RadixThemesHeading,IconButton as RadixThemesIconButton,Spinner as RadixThemesSpinner,Text as RadixThemesText,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isNotNullOrUndefined,isTrue} from "$/utils/state"
import DebounceInput from "react-debounce-input"
import {Delete as LucideDelete} from "lucide-react"
import {jsx} from "@emotion/react"




function Textfield__root_6c4915b5bf1ff54f37c5e30b0a305dac () {
  const reflex___state____state__reflex_proj___reflex_proj____auto_complete_state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____auto_complete_state)



  return (
    jsx(RadixThemesTextField.Root,{css:({ ["isDisabled"] : true, ["color"] : "#888888", ["position"] : "absolute", ["zIndex"] : 1, ["width"] : "100%", ["height"] : "40px", ["background"] : "black", ["borderColor"] : "gray.200", ["&:focus"] : ({ ["borderColor"] : "gray.200" }) }),value:(isNotNullOrUndefined((reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.query_rx_state_+reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.in_line_suggestion_rx_state_)) ? (reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.query_rx_state_+reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.in_line_suggestion_rx_state_) : "")},)
  )
}


function Debounceinput_f3cb940fbc1d082fb82c437fa7cd6f12 () {
  const reflex___state____state__reflex_proj___reflex_proj____auto_complete_state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____auto_complete_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_b8ab99b3b6a2d436178114bbbd9ce7b8 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____auto_complete_state.update_query", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])
const on_key_down_f64269df86713d13d81b70a0418a3c71 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____auto_complete_state.handle_key_down", ({ ["key"] : _e?.["key"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["position"] : "absolute", ["zIndex"] : 2, ["width"] : "100%", ["height"] : "40px", ["background"] : "transparent", ["color"] : "white", ["borderColor"] : "gray.200", ["&:placeholder"] : ({ ["color"] : "gray.400" }), ["&:focus"] : ({ ["borderColor"] : "#3b82f6", ["boxShadow"] : "0 0 0 1px #3b82f6", ["zIndex"] : 2 }) }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_b8ab99b3b6a2d436178114bbbd9ce7b8,onKeyDown:on_key_down_f64269df86713d13d81b70a0418a3c71,placeholder:"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043e\u043a...",size:"2",value:(isNotNullOrUndefined(reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.query_rx_state_) ? reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.query_rx_state_ : "")},)
  )
}


function Iconbutton_02f0d13da3cc85da586e83b4e2328c15 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_51e0d96ad8d7960e20452dc9a6f3ff3b = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____auto_complete_state.clear_input", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesIconButton,{css:({ ["padding"] : "6px" }),onClick:on_click_51e0d96ad8d7960e20452dc9a6f3ff3b,size:"2",variant:"ghost"},jsx(LucideDelete,{size:24},))
  )
}


function Fragment_e47eb0dcf6df371caf362318c87e9dbe () {
  const reflex___state____state__reflex_proj___reflex_proj____auto_complete_state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____auto_complete_state)



  return (
    jsx(Fragment,{},(isTrue(reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.query_rx_state_)?(jsx(Fragment,{},jsx(Iconbutton_02f0d13da3cc85da586e83b4e2328c15,{},))):(jsx(Fragment,{},))))
  )
}


function Fragment_38ece412b3dfc2f41109c112310c6e56 () {
  const reflex___state____state__reflex_proj___reflex_proj____auto_complete_state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____auto_complete_state)



  return (
    jsx(Fragment,{},(reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.loading_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["padding"] : "0.5em" }),direction:"row",gap:"3"},jsx(RadixThemesSpinner,{size:"2"},),jsx(RadixThemesText,{as:"p",size:"2"},"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...")))):(jsx(Fragment,{},))))
  )
}


function Flex_dede2514c5da8c1ae4188663d8f85517 () {
  const reflex___state____state__reflex_proj___reflex_proj____auto_complete_state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____auto_complete_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"0"},jsx(Fragment_38ece412b3dfc2f41109c112310c6e56,{},),Array.prototype.map.call(reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.word_suggestions_rx_state_ ?? [],((suggestion_rx_state_,idx_rx_state_)=>(jsx(Fragment,{key:idx_rx_state_},((idx_rx_state_?.valueOf?.() === reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.selected_index_rx_state_?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesButton,{css:({ ["width"] : "100%", ["backgroundColor"] : "rgba(59, 130, 246, 0.1)", ["&:hover"] : ({ ["backgroundColor"] : "rgba(59, 130, 246, 0.2)" }), ["padding"] : "0.5em" }),onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____auto_complete_state.select_suggestion", ({ ["suggestion"] : ({ ["button"] : _e?.["button"], ["buttons"] : _e?.["buttons"], ["client_x"] : _e?.["clientX"], ["client_y"] : _e?.["clientY"], ["alt_key"] : _e?.["altKey"], ["ctrl_key"] : _e?.["ctrlKey"], ["meta_key"] : _e?.["metaKey"], ["shift_key"] : _e?.["shiftKey"] }) }), ({  })))], [_e], ({  }))))},jsx(RadixThemesText,{as:"p",size:"2"},suggestion_rx_state_)))):(jsx(Fragment,{},jsx(RadixThemesButton,{css:({ ["width"] : "100%", ["padding"] : "0.5em" }),onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.reflex_proj___reflex_proj____auto_complete_state.select_suggestion", ({ ["suggestion"] : ({ ["button"] : _e?.["button"], ["buttons"] : _e?.["buttons"], ["client_x"] : _e?.["clientX"], ["client_y"] : _e?.["clientY"], ["alt_key"] : _e?.["altKey"], ["ctrl_key"] : _e?.["ctrlKey"], ["meta_key"] : _e?.["metaKey"], ["shift_key"] : _e?.["shiftKey"] }) }), ({  })))], [_e], ({  })))),variant:"ghost"},jsx(RadixThemesText,{as:"p",size:"2"},suggestion_rx_state_))))))))))
  )
}


function Fragment_41b70894866de0cfce930d540dec0382 () {
  const reflex___state____state__reflex_proj___reflex_proj____auto_complete_state = useContext(StateContexts.reflex___state____state__reflex_proj___reflex_proj____auto_complete_state)



  return (
    jsx(Fragment,{},(reflex___state____state__reflex_proj___reflex_proj____auto_complete_state.show_suggestions_rx_state_?(jsx(Fragment,{},jsx(RadixThemesCard,{css:({ ["marginTop"] : "0.5em", ["width"] : "100%", ["maxHeight"] : "200px", ["overflowY"] : "auto", ["zIndex"] : 10 })},jsx(Flex_dede2514c5da8c1ae4188663d8f85517,{},)))):(jsx(Fragment,{},))))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%", ["height"] : "100vh" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start", ["padding"] : "1em" }),direction:"column",gap:"2"},jsx(RadixThemesHeading,{size:"5"},"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0441\u0432\u043e\u0439 \u044d\u043c\u0435\u0439\u043b, \u0430 \u043c\u044b \u0432\u0430\u043c \u043f\u043e\u043c\u043e\u0436\u0435\u043c!"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray" })},"\u041d\u0430\u0447\u043d\u0438\u0442\u0435 \u0432\u0432\u043e\u0434\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442:"),jsx(RadixThemesBox,{css:({ ["position"] : "relative", ["@media screen and (min-width: 0)"] : ({ ["width"] : "90vw" }), ["@media screen and (min-width: 30em)"] : ({ ["width"] : "60vw" }), ["@media screen and (min-width: 48em)"] : ({ ["width"] : "50vw" }), ["@media screen and (min-width: 62em)"] : ({ ["width"] : "40vw" }), ["@media screen and (min-width: 80em)"] : ({ ["width"] : "30vw" }) })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",gap:"3"},jsx(RadixThemesBox,{css:({ ["position"] : "relative", ["height"] : "40px", ["width"] : "100%" })},jsx(Textfield__root_6c4915b5bf1ff54f37c5e30b0a305dac,{},),jsx(Debounceinput_f3cb940fbc1d082fb82c437fa7cd6f12,{},)),jsx(Fragment_e47eb0dcf6df371caf362318c87e9dbe,{},)),jsx(Fragment_41b70894866de0cfce930d540dec0382,{},)))),jsx("title",{},"ReflexProj | Email"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}