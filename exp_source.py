#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on November 25, 2019, at 20:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from random import sample
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import json
from psychopy.hardware import keyboard

# Getting the sound conditions to be random

SOUND_CONDITIONS = ['sounds/lofi/buddy.wav', 'sounds/lofi/happy.wav', 'sounds/lofi/pink1.wav']
SOUND_CONDITIONS = sample(SOUND_CONDITIONS, len(SOUND_CONDITIONS))



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'posner'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + \
    u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

with open(f'./data/{expInfo["participant"]}_{expName}_{expInfo["date"]}.json', 'x') as f:
    json_file = {num_id+ 1: condition for num_id, condition in enumerate(SOUND_CONDITIONS)}
    json.dump(json_file, f)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='E:\\Data Science and Coding\\Python\\Studying\\Final Year Project\\posner.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# this outputs to the screen, not a file
logging.console.setLevel(logging.WARNING)

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=1,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
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
fixation = visual.TextStim(win=win, name='fixation',
                           text='+',
                           font='Arial',
                           pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                           color='white', colorSpace='rgb', opacity=1,
                           languageStyle='LTR',
                           depth=0.0)
cue = visual.ImageStim(
    win=win,
    name='cue', units='height',
    image='images/arrow-left.png', mask=None,
    ori=1.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
target = visual.ImageStim(
    win=win,
    name='target', units='height',
    image='images/circle_red.png', mask=None,
    ori=0, pos=[0, 0], size=(0.20, 0.20),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp = keyboard.Keyboard()





# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
break_text = visual.TextStim(win=win, name='break_text',
                             text='Please take a minute break',
                             font='Arial',
                             pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
# to track time remaining of each (non-slip) routine
routineTimer = core.CountdownTimer()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=9, method='random',
                          extraInfo=expInfo, originPath=-1,
                          trialList=[None],
                          seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

sound_condition = -1



for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))

    # set up handler to look after randomisation of conditions etc
    posner_task = data.TrialHandler(nReps=1, method='random',
                                    extraInfo=expInfo, originPath=-1,
                                    trialList=data.importConditions(
                                        'conditions.csv'),
                                    seed=None, name='posner_task')
    thisExp.addLoop(posner_task)  # add the loop to the experiment
    # so we can initialise stimuli with some values
    thisPosner_task = posner_task.trialList[0]
    # abbreviate parameter names if possible (e.g. rgb = thisPosner_task.rgb)
    if thisPosner_task != None:
        for paramName in thisPosner_task:
            exec('{} = thisPosner_task[paramName]'.format(paramName))

    sound_condition += 1

    
    
    background_sound = sound.Sound(SOUND_CONDITIONS[sound_condition], startTime=0, stopTime=60)

    for thisPosner_task in posner_task:
        currentLoop = posner_task
        # abbreviate parameter names if possible (e.g. rgb = thisPosner_task.rgb)
        if thisPosner_task != None:
            for paramName in thisPosner_task:
                exec('{} = thisPosner_task[paramName]'.format(paramName))

        # ------Prepare to start Routine "trial"-------
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        cue.setOri(cueOri)
        target.setPos([targetX, 0])
        key_resp.keys = []
        key_resp.rt = []

        # background_sound = sound.Sound(SOUND_CONDITIONS[randint(low=0, high=2)], startTime=0, stopTime=60)
        
        if posner_task.thisN == 0:
            
            background_sound.play()
        # keep track of which components have finished
        trialComponents = [fixation, cue, target, key_resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        # t0 is time of first possible flip
        trialClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True

        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            # number of completed frames (so 0 is the first frame)
            frameN = frameN + 1
            # update/draw components on each frame

            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                win.timeOnFlip(fixation, 'tStartRefresh')
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # time at next scr refresh
                    win.timeOnFlip(fixation, 'tStopRefresh')
                    fixation.setAutoDraw(False)

            # *cue* updates
            if cue.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                cue.frameNStart = frameN  # exact frame index
                cue.tStart = t  # local t and not account for scr refresh
                cue.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                win.timeOnFlip(cue, 'tStartRefresh')
                cue.setAutoDraw(True)
            if cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    cue.tStop = t  # not accounting for scr refresh
                    cue.frameNStop = frameN  # exact frame index
                    # time at next scr refresh
                    win.timeOnFlip(cue, 'tStopRefresh')
                    cue.setAutoDraw(False)

            # *target* updates
            if target.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                target.frameNStart = frameN  # exact frame index
                target.tStart = t  # local t and not account for scr refresh
                target.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                win.timeOnFlip(target, 'tStartRefresh')
                target.setAutoDraw(True)
            if target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    target.tStop = t  # not accounting for scr refresh
                    target.frameNStop = frameN  # exact frame index
                    # time at next scr refresh
                    win.timeOnFlip(target, 'tStopRefresh')
                    target.setAutoDraw(False)

            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                win.timeOnFlip(key_resp, 'tStartRefresh')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                # clear events on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # time at next scr refresh
                    win.timeOnFlip(key_resp, 'tStopRefresh')
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(
                    keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed

                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp.keys = theseKeys.name  # just the last key pressed
                    key_resp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False

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
        posner_task.addData('fixation.started', fixation.tStartRefresh)
        posner_task.addData('fixation.stopped', fixation.tStopRefresh)
        posner_task.addData('cue.started', cue.tStartRefresh)
        posner_task.addData('cue.stopped', cue.tStopRefresh)
        posner_task.addData('target.started', target.tStartRefresh)
        posner_task.addData('target.stopped', target.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
                key_resp.corr = 1  # correct non-response
            else:
                key_resp.corr = 0  # failed to respond (incorrectly)
        # store data for posner_task (TrialHandler)
        posner_task.addData('key_resp.keys', key_resp.keys)
        posner_task.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            posner_task.addData('key_resp.rt', key_resp.rt)
        posner_task.addData('key_resp.started', key_resp.tStartRefresh)
        posner_task.addData('key_resp.stopped', key_resp.tStopRefresh)
        if posner_task.thisN == 7:
            background_sound.stop()
        thisExp.nextEntry()

    # completed 2 repeats of 'posner_task'

    # ------Prepare to start Routine "break_2"-------
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
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *break_text* updates
        if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(break_text, 'tStartRefresh')
            break_text.setAutoDraw(True)
        if break_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_text.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                break_text.tStop = t  # not accounting for scr refresh
                break_text.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(break_text, 'tStopRefresh')
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

# completed 9 repeats of 'block'


# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
