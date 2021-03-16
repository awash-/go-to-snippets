Sub SplitAddresses()

Dim c As Range

    For Each c In Selection.Cells
        If c.Value = "" Then
            c.FillDown
        End If
    Next c

End Sub
