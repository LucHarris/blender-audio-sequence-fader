class AudioSequenceFader(bpy.types.Operator):
    """A Sequence Editor Panel for fading audio sequences."""
    bl_idname = "sequencer.audio_sequence_fader" # refer to in gui.py layout 
    bl_label = "Audio Sequence Fader" 


    def sortByStartFrame(e):
        return e.frame_start + e.frame_offset_start

    def execute(self,context):
        # todo add variables to gui
        fade  = 30 
        staggered = False # todo list

        # sequence 
        seq = bpy.context.scene.sequence_editor 

        # channel from active strip
        channel = seq.active_strip.channel

        # array for sequences to fade
        channelStrips = []

        # adds audio strips to array from active channel
        for strip in seq.sequences_all:
            if (strip.channel == channel):
                if(strip.type == "SOUND"):
                    channelStrips.append(strip)

        # slope effect
        channelStrips.sort(key=SortByStartFrame)

        for i,s in enumerate(channelStrips):
            # offset channel 
            if( staggered):
                s.channel += i % 2
            else: 
                s.channel += i
            # offset frame
            s.frame_start -= fade * i
            # select for sequence operation 
            s.select = True;
            # fade in
            bpy.context.scene.frame_current = s.frame_final_start + fade
            bpy.ops.sequencer.fades_add(type='CURSOR_TO')
            # fade out
            bpy.context.scene.frame_current = s.frame_final_end - fade
            bpy.ops.sequencer.fades_add(type='CURSOR_FROM')
        
        return {'FINISHED'}