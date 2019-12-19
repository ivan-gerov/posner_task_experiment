#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on November 28, 2019, at 10:15
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
                                
from random import sample
import json
                                
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



### Start of Custom Functions ###

# Ensure that relative paths start from the same directory as this script

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
os.chdir('..')
_thisDir = os.path.relpath(os.getcwd())

# Seting the Posner task repetitions and time per one attention task block
# 22 sec is the lowest the system can do due to the distribution of valid to invalid cues (One loop in the attention block is 8 reps of the Posner task, i.e. 6 valid 2 invalid cues)
TIME_PER_ATTENTION_BLOCK = 22  # 240 seconds, 1 posner = 2.7 seconds 


def getNumberOfPosnerReps(TIME_PER_ATTENTION_BLOCK=TIME_PER_ATTENTION_BLOCK):
    """ 
    Returns the number of repetitions a posner task trial needs to do, in order to complete
    the TIME_PER_ATTENTION_BLOCK desired time.

    One posner task trial is 2.7 sec.

    e.g. If TIME_PER_ATTENTION_BLOCK is 240 sec, the number of reps is 88.

    """
    POSNER_TRIAL = 2.7
    numOfReps = np.floor(TIME_PER_ATTENTION_BLOCK / POSNER_TRIAL)
    return numOfReps


# Getting the sound conditions to be random
SOUND_CONDITIONS = ['sounds/silence.wav',
                    'sounds/lofi_track.wav', 'sounds/pink_track.wav']
SOUND_CONDITIONS = sample(SOUND_CONDITIONS, len(SOUND_CONDITIONS))


def organizeParticipantSessionFolder(expInfo, expName, _thisDir):
    """ 
    Checks if a the following dir exits - "./data/session_name" and
    if not creates one.

    Returns the file_name_stem = "participant_name"_"datetime"
    """
    session_folder_path = f"{_thisDir}/data/{expInfo['participant']}_{expName}"
    if os.path.exists(session_folder_path) == False:
        os.mkdir(f'{session_folder_path}')
    FILE_NAME_STEM = f'{session_folder_path}/{expInfo["participant"]}_{expName}_{expInfo["date"]}'
    return FILE_NAME_STEM


def saveSoundConditionSequence(file_name_stem, SOUND_CONDITIONS=SOUND_CONDITIONS):
    """ 
    Saves info about the experiment and the sound conditions that the randomizer selected 
    in a JSON file with the following format

    "participant_name"_"experiment_name"_"datetime".json

    """
    json_file_name = file_name_stem + '.json'

    if os.path.exists(json_file_name) == True:
        file_mode = 'w'
    elif os.path.exists(json_file_name) == False:
        file_mode = 'x'

    with open(json_file_name, file_mode) as f:
        json_string = {num_id + 1: condition for num_id,
                    condition in enumerate(SOUND_CONDITIONS)}
        json.dump(json_string, f)
        f.close()

### End of Custom Functions ###


# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'posner'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

### Start-Of-Custom-Code ###

# Make participant session dir and return file_name_stem = "participant_name"_"experiment_name"_"datetime"
FILE_NAME_STEM = organizeParticipantSessionFolder(
    expInfo, expName, _thisDir)

# Ensure that the sequence of sound conditions is outputted to JSON
saveSoundConditionSequence(FILE_NAME_STEM)   
    
### End-Of-Custom-Code ###


# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=True, saveWideText=True,
    dataFileName=FILE_NAME_STEM)
# save a log file for detail verbose info
logFile = logging.LogFile(FILE_NAME_STEM+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=-1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation_1 = visual.TextStim(win=win, name='fixation_1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
cue = visual.ImageStim(
    win=win,
    name='cue', units='height', 
    image='images/arrow-left.png', mask=None,
    ori=1.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
target = visual.ImageStim(
    win=win,
    name='target', units='height', 
    image='images/circle_red.png', mask=None,
    ori=0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)





# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
break_text = visual.TextStim(win=win, name='break_text',
    text='Please take a minute break',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))
        
### Start-Of-Custom-Code ###

# Initialize our sound_condition tracker as -1
sound_condition = -1

### End-Of-Custom-Code ###

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    posner_task = data.TrialHandler(nReps=getNumberOfPosnerReps()/8, method='random', 
        extraInfo=expInfo,
        trialList=data.importConditions('conditions.csv'),
        seed=None, name='posner_task')
    thisExp.addLoop(posner_task)  # add the loop to the experiment
    thisPosner_task = posner_task.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPosner_task.rgb)
    if thisPosner_task != None:
        for paramName in thisPosner_task:
            exec('{} = thisPosner_task[paramName]'.format(paramName))
            
    ### Start-Of-Custom-Code ###

    sound_condition += 1

    background_sound = sound.Sound(SOUND_CONDITIONS[sound_condition])

    ### End-Of-Custom-Code ###
    
    for thisPosner_task in posner_task:
        currentLoop = posner_task
        # abbreviate parameter names if possible (e.g. rgb = thisPosner_task.rgb)
        if thisPosner_task != None:
            for paramName in thisPosner_task:
                exec('{} = thisPosner_task[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.700000)
        # update component parameters for each repeat
        cue.setOri(cueOri)
        target.setPos([targetX, 0])
        correct_key_resp = keyboard.Keyboard()
        
        ### Start-Of-Custom-Code ###

        if posner_task.thisN == 0:
            background_sound.play()

        ### End-Of-Custom-Code ###
        
        
        early_resp = keyboard.Keyboard()
        # keep track of which components have finished
        trialComponents = [fixation_1, fixation_2, cue, target, correct_key_resp, early_resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_1* updates
            if t >= 0.0 and fixation_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_1.tStart = t  # not accounting for scr refresh
                fixation_1.frameNStart = frameN  # exact frame index
                win.timeOnFlip(fixation_1, 'tStartRefresh')  # time at next scr refresh
                fixation_1.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_1.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                fixation_1.tStop = t  # not accounting for scr refresh
                fixation_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_1, 'tStopRefresh')  # time at next scr refresh
                fixation_1.setAutoDraw(False)
            
            # *fixation_2* updates
            if t >= 1.2 and fixation_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_2.tStart = t  # not accounting for scr refresh
                fixation_2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(True)
            frameRemains = 2.7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_2.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(False)
            
            # *cue* updates
            if t >= 0.5 and cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                cue.tStart = t  # not accounting for scr refresh
                cue.frameNStart = frameN  # exact frame index
                win.timeOnFlip(cue, 'tStartRefresh')  # time at next scr refresh
                cue.setAutoDraw(True)
            frameRemains = 0.5 + 0.7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cue.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                cue.tStop = t  # not accounting for scr refresh
                cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue, 'tStopRefresh')  # time at next scr refresh
                cue.setAutoDraw(False)
            
            # *target* updates
            if t >= 1.7 and target.status == NOT_STARTED:
                # keep track of start time/frame for later
                target.tStart = t  # not accounting for scr refresh
                target.frameNStart = frameN  # exact frame index
                win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
                target.setAutoDraw(True)
            frameRemains = 1.7 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if target.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
            
            # *correct_key_resp* updates
            if t >= 1.7 and correct_key_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                correct_key_resp.tStart = t  # not accounting for scr refresh
                correct_key_resp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(correct_key_resp, 'tStartRefresh')  # time at next scr refresh
                correct_key_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(correct_key_resp.clock.reset)  # t=0 on next screen flip
                correct_key_resp.clearEvents(eventType='keyboard')
            frameRemains = 1.7 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if correct_key_resp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                correct_key_resp.tStop = t  # not accounting for scr refresh
                correct_key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_key_resp, 'tStopRefresh')  # time at next scr refresh
                correct_key_resp.status = FINISHED
            if correct_key_resp.status == STARTED:
                theseKeys = correct_key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if correct_key_resp.keys == []:  # then this was the first keypress
                        correct_key_resp.keys = theseKeys.name  # just the first key pressed
                        correct_key_resp.rt = theseKeys.rt
                        # was this 'correct'?
                        if (correct_key_resp.keys == str(corrAns)) or (correct_key_resp.keys == corrAns):
                            correct_key_resp.corr = 1
                        else:
                            correct_key_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *early_resp* updates
            if t >= 0.5 and early_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                early_resp.tStart = t  # not accounting for scr refresh
                early_resp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(early_resp, 'tStartRefresh')  # time at next scr refresh
                early_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(early_resp.clock.reset)  # t=0 on next screen flip
                early_resp.clearEvents(eventType='keyboard')
            frameRemains = 1.7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if early_resp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                early_resp.tStop = t  # not accounting for scr refresh
                early_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(early_resp, 'tStopRefresh')  # time at next scr refresh
                early_resp.status = FINISHED
            if early_resp.status == STARTED:
                theseKeys = early_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if early_resp.keys == []:  # then this was the first keypress
                        early_resp.keys = theseKeys.name  # just the first key pressed
                        early_resp.rt = theseKeys.rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        posner_task.addData('fixation_1.started', fixation_1.tStartRefresh)
        posner_task.addData('fixation_1.stopped', fixation_1.tStopRefresh)
        posner_task.addData('fixation_2.started', fixation_2.tStartRefresh)
        posner_task.addData('fixation_2.stopped', fixation_2.tStopRefresh)
        posner_task.addData('cue.started', cue.tStartRefresh)
        posner_task.addData('cue.stopped', cue.tStopRefresh)
        posner_task.addData('target.started', target.tStartRefresh)
        posner_task.addData('target.stopped', target.tStopRefresh)
        # check responses
        if correct_key_resp.keys in ['', [], None]:  # No response was made
            correct_key_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               correct_key_resp.corr = 1;  # correct non-response
            else:
               correct_key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for posner_task (TrialHandler)
        posner_task.addData('correct_key_resp.keys',correct_key_resp.keys)
        posner_task.addData('correct_key_resp.corr', correct_key_resp.corr)
        if correct_key_resp.keys != None:  # we had a response
            posner_task.addData('correct_key_resp.rt', correct_key_resp.rt)
        posner_task.addData('correct_key_resp.started', correct_key_resp.tStartRefresh)
        posner_task.addData('correct_key_resp.stopped', correct_key_resp.tStopRefresh)
        
        ### Start-Of-Custom-Code ###
        
        if posner_task.thisN == getNumberOfPosnerReps() - 1:  # we subtract 1 due to Python 0 indexing
            background_sound.stop()

        ### End-Of-Custom-Code ###
        
        
        # check responses
        if early_resp.keys in ['', [], None]:  # No response was made
            early_resp.keys = None
        posner_task.addData('early_resp.keys',early_resp.keys)
        if early_resp.keys != None:  # we had a response
            posner_task.addData('early_resp.rt', early_resp.rt)
        posner_task.addData('early_resp.started', early_resp.tStartRefresh)
        posner_task.addData('early_resp.stopped', early_resp.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'posner_task'
    
    
    # ------Prepare to start Routine "break_2"-------
    t = 0
    break_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [break_text]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        if t >= 0.0 and break_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_text.tStart = t  # not accounting for scr refresh
            break_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            break_text.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if break_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            break_text.tStop = t  # not accounting for scr refresh
            break_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(break_text, 'tStopRefresh')  # time at next scr refresh
            break_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('break_text.started', break_text.tStartRefresh)
    block.addData('break_text.stopped', break_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'block'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)

### Start-Of-Custom-Code ###

thisExp.saveAsWideText(FILE_NAME_STEM+'.csv')
thisExp.saveAsPickle(FILE_NAME_STEM)    
    
### End-Of-Custom-Code ###


logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
