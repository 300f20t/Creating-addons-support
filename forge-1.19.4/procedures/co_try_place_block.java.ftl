if (${input$entity} instanceof ServerPlayer _ServerPlayer) {
PlacementHandler.tryPlaceBlock(_ServerPlayer, world.getBlockState(BlockPos.containing(${input$X}, ${input$Y}, ${input$Z})), ${input$dir}, null);
}