if(${input$entity} instanceof Entity || ${input$entity} instanceof BlockEntity) {
	${input$entity}.set${field$name}(${input$value});
}