#!/bin/bash

# liftover 実行

paftools.js liftover Bd1_t314-q192.cs_long.paf Bd21-3xBd21_markers.bed > Bd1_Bd21-3xBd21_markers.liftover.bed
paftools.js liftover Bd2_t314-q192.cs_long.paf Bd21-3xBd21_markers.bed > Bd2_Bd21-3xBd21_markers.liftover.bed
paftools.js liftover Bd3_t314-q192.cs_long.paf Bd21-3xBd21_markers.bed > Bd3_Bd21-3xBd21_markers.liftover.bed
paftools.js liftover Bd4_t314-q192.cs_long.paf Bd21-3xBd21_markers.bed > Bd4_Bd21-3xBd21_markers.liftover.bed
paftools.js liftover Bd5_t314-q192.cs_long.paf Bd21-3xBd21_markers.bed > Bd5_Bd21-3xBd21_markers.liftover.bed

paftools.js liftover Bd1_t314-q192.cs_long.paf Bd21xKoz4_markers.bed > Bd1_Bd21xKoz4_markers.liftover.bed
paftools.js liftover Bd2_t314-q192.cs_long.paf Bd21xKoz4_markers.bed > Bd2_Bd21xKoz4_markers.liftover.bed
paftools.js liftover Bd3_t314-q192.cs_long.paf Bd21xKoz4_markers.bed > Bd3_Bd21xKoz4_markers.liftover.bed
paftools.js liftover Bd4_t314-q192.cs_long.paf Bd21xKoz4_markers.bed > Bd4_Bd21xKoz4_markers.liftover.bed
paftools.js liftover Bd5_t314-q192.cs_long.paf Bd21xKoz4_markers.bed > Bd5_Bd21xKoz4_markers.liftover.bed
