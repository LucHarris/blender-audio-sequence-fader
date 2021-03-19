import bpy

class FaderPanel(bpy.types.Panel):
    """A Sequence Editor Panel for fading audio sequences."""
    bl_label =  "Audio Fading"
    bl_idname = "SCENE_PT_audio_sequence_fading"
    bl_space_type = "SEQUENCE_EDITOR"
    bl_region_type = "UI"
    bl_category = 'Strip'

    @classmethod
    def poll(cls, context):
        return context.space_data.view_type == 'SEQUENCER' and len(context.selected_sequences) == 1

    def draw(self, context):
        layout = self.layout

        layout.label(text = "Active Channel: " + str(context.scene.sequence_editor.active_strip.channel))
        layout.operator("sequencer.audio_sequence_fader", text = "Fade Channel") # bl_idname from operators

