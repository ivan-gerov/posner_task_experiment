#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on November 27, 2019, at 20:20
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

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'posner'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Data Science and Coding\\Python\\Studying\\Final Year Project\\posner_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

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
correct_key_resp = keyboard.Keyboard()



background_sound= sound.Sound('sounds/silence.wav')
early_resp = keyboard.Keyboard()

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
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    posner_task = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.csv'),
        seed=None, name='posner_task')
    thisExp.addLoop(posner_task)  # add the loop to the experiment
    thisPosner_task = posner_task.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPosner_task.rgb)
    if thisPosner_task != None:
        for paramName in thisPosner_task:
            exec('{} = thisPosner_task[paramName]'.format(paramName))
    
    for thisPosner_task in posner_task:
        currentLoop = posner_task
        # abbreviate parameter names if possible (e.g. rgb = thisPosner_task.rgb)
        if thisPosner_task != None:
            for paramName in thisPosner_task:
                exec('{} = thisPosner_task[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        routineTimer.add(2.700000)
        # update component parameters for each repeat
        cue.setOri(cueOri)
        target.setPos([targetX, 0])
        correct_key_resp.keys = []
        correct_key_resp.rt = []
        if posner_task.thisN == 0:
            background_sound.play()
        early_resp.keys = []
        early_resp.rt = []
        # keep track of which components have finished
        trialComponents = [fixation_1, fixation_2, cue, target, correct_key_resp, early_resp]
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
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_1* updates
            if fixation_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_1.frameNStart = frameN  # exact frame index
                fixation_1.tStart = t  # local t and not account for scr refresh
                fixation_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_1, 'tStartRefresh')  # time at next scr refresh
                fixation_1.setAutoDraw(True)
            if fixation_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_1.tStop = t  # not accounting for scr refresh
                    fixation_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_1, 'tStopRefresh')  # time at next scr refresh
                    fixation_1.setAutoDraw(False)
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2.7-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
                    fixation_2.setAutoDraw(False)
            
            # *cue* updates
            if cue.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                cue.frameNStart = frameN  # exact frame index
                cue.tStart = t  # local t and not account for scr refresh
                cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue, 'tStartRefresh')  # time at next scr refresh
                cue.setAutoDraw(True)
            if cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue.tStartRefresh + 0.7-frameTolerance:
                    # keep track of stop time/frame for later
                    cue.tStop = t  # not accounting for scr refresh
                    cue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cue, 'tStopRefresh')  # time at next scr refresh
                    cue.setAutoDraw(False)
            
            # *target* updates
            if target.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                target.frameNStart = frameN  # exact frame index
                target.tStart = t  # local t and not account for scr refresh
                target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
                target.setAutoDraw(True)
            if target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    target.tStop = t  # not accounting for scr refresh
                    target.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                    target.setAutoDraw(False)
            
            # *correct_key_resp* updates
            waitOnFlip = False
            if correct_key_resp.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                correct_key_resp.frameNStart = frameN  # exact frame index
                correct_key_resp.tStart = t  # local t and not account for scr refresh
                correct_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(correct_key_resp, 'tStartRefresh')  # time at next scr refresh
                correct_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(correct_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(correct_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if correct_key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > correct_key_resp.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    correct_key_resp.tStop = t  # not accounting for scr refresh
                    correct_key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(correct_key_resp, 'tStopRefresh')  # time at next scr refresh
                    correct_key_resp.status = FINISHED
            if correct_key_resp.status == STARTED and not waitOnFlip:
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
            waitOnFlip = False
            if early_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                early_resp.frameNStart = frameN  # exact frame index
                early_resp.tStart = t  # local t and not account for scr refresh
                early_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(early_resp, 'tStartRefresh')  # time at next scr refresh
                early_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(early_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(early_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if early_resp.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    early_resp.tStop = t  # not accounting for scr refresh
                    early_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(early_resp, 'tStopRefresh')  # time at next scr refresh
                    early_resp.status = FINISHED
            if early_resp.status == STARTED and not waitOnFlip:
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
        if posner_task.thisN == 7:
            background_sound.stop()
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
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            break_text.setAutoDraw(True)
        if break_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_text.tStartRefresh + 10-frameTolerance:
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
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
