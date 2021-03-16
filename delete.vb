Sub DeleteRows()
    Dim rng As Range
    Dim pos As Integer
    Set rng = ActiveSheet.UsedRange
    
    For i = rng.Cells.Count To 1 Step -1
        pos = InStr(LCase(rng.Item(i).Value), LCase("summer camp"))
        If pos > 0 Then
            rng.Item(i).EntireRow.Delete
        End If
    Next i
End Sub
